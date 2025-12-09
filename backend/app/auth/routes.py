"""Authentication routes"""
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session, select
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import secrets
from datetime import datetime

from app.database import get_session
from app.models import User
from app.auth.password import hash_password, verify_password
from app.auth.jwt import create_access_token
from app.auth.dependencies import get_current_user
from app.auth.email_service import send_verification_email, send_welcome_email

router = APIRouter(prefix="/api/v1/auth", tags=["authentication"])


# Schemas
class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)
    full_name: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    full_name: Optional[str]
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


@router.post("/register", response_model=UserResponse, status_code=201)
def register(
    user_data: UserRegister,
    session: Session = Depends(get_session)
):
    """Register a new user and send verification email"""

    # Check if user already exists
    result = session.execute(select(User).where(User.email == user_data.email))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Create verification token
    verification_token = secrets.token_urlsafe(32)

    # Create new user
    new_user = User(
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        full_name=user_data.full_name,
        is_active=False,  # Not active until verified
        is_verified=False,
        verification_token=verification_token,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    # Send verification email
    send_verification_email(
        to_email=new_user.email,
        verification_token=verification_token,
        user_name=new_user.full_name
    )

    return new_user


@router.post("/login")
def login(
    user_data: UserLogin,
    response: Response,
    session: Session = Depends(get_session)
):
    """Login user and return JWT token in cookie"""

    # Find user by email
    result = session.execute(select(User).where(User.email == user_data.email))
    user = result.scalar_one_or_none()

    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Please verify your email address first"
        )

    # Create access token
    access_token = create_access_token(data={"sub": user.id})

    # Set cookie (httpOnly for security)
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        max_age=60 * 60 * 24 * 7,  # 7 days
        samesite="lax",
        secure=False  # Set to True in production with HTTPS
    )

    return TokenResponse(
        access_token=access_token,
        user=UserResponse.model_validate(user)
    )


@router.post("/verify-email")
def verify_email(
    token: str,
    session: Session = Depends(get_session)
):
    """Verify user email with token"""

    # Find user by verification token
    result = session.execute(
        select(User).where(User.verification_token == token)
    )
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid verification token"
        )

    if user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already verified"
        )

    # Verify user
    user.is_verified = True
    user.is_active = True
    user.verification_token = None  # Clear token
    user.updated_at = datetime.utcnow()

    session.add(user)
    session.commit()
    session.refresh(user)

    # Send welcome email
    send_welcome_email(to_email=user.email, user_name=user.full_name)

    return {"message": "Email verified successfully", "user": UserResponse.model_validate(user)}


@router.post("/logout")
def logout(response: Response):
    """Logout user by clearing cookie"""
    response.delete_cookie(key="access_token")
    return {"message": "Logged out successfully"}


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    """Get current authenticated user"""
    return current_user


@router.post("/resend-verification")
def resend_verification(
    email: EmailStr,
    session: Session = Depends(get_session)
):
    """Resend verification email"""

    result = session.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if not user:
        # Don't reveal if user exists or not (security)
        return {"message": "If the email exists, a verification link has been sent"}

    if user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already verified"
        )

    # Generate new token
    verification_token = secrets.token_urlsafe(32)
    user.verification_token = verification_token
    user.updated_at = datetime.utcnow()

    session.add(user)
    session.commit()

    # Send verification email
    send_verification_email(
        to_email=user.email,
        verification_token=verification_token,
        user_name=user.full_name
    )

    return {"message": "Verification email sent"}
