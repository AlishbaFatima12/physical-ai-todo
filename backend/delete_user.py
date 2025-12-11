"""
Quick script to delete a user by email
"""
import asyncio
from sqlmodel import Session, select
from app.database import engine
from app.models import User

async def delete_user_by_email(email: str):
    """Delete a user by email"""
    with Session(engine) as session:
        # Find user
        result = session.execute(select(User).where(User.email == email.lower()))
        user = result.scalar_one_or_none()

        if user:
            print(f"Found user: {user.email} (ID: {user.id})")
            print(f"  Created: {user.created_at}")
            print(f"  Verified: {user.is_verified}")

            # Delete user
            session.delete(user)
            session.commit()
            print(f"[SUCCESS] Deleted user: {user.email}")
            return True
        else:
            print(f"[ERROR] User not found: {email}")
            return False

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python delete_user.py <email>")
        sys.exit(1)

    email = sys.argv[1]
    asyncio.run(delete_user_by_email(email))
