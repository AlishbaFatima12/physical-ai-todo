"""
Database configuration and connection management for Neon DB.

Uses SQLModel with async asyncpg driver for PostgreSQL.
"""

import os
from typing import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

# Load environment variables
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create async engine
engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    echo=True,  # Log SQL queries (set to False in production)
    pool_pre_ping=True,  # Verify connections before using
    pool_recycle=3600,  # Recycle connections after 1 hour
    pool_size=5,  # Connection pool size
    max_overflow=10,  # Max overflow connections
)

# Create async session factory
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def init_db() -> None:
    """
    Initialize database by creating all tables defined in SQLModel metadata.

    This should be run once during application startup or via CLI.
    """
    async with engine.begin() as conn:
        # Create all tables
        await conn.run_sync(SQLModel.metadata.create_all)

    print("✓ Database tables created successfully")


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency function to get database session for FastAPI routes.

    Usage:
        @app.get("/tasks")
        async def get_tasks(session: AsyncSession = Depends(get_session)):
            ...

    Yields:
        AsyncSession: Database session that automatically commits/rollbacks
    """
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def close_db() -> None:
    """
    Close database engine and all connections.

    This should be called during application shutdown.
    """
    await engine.dispose()
    print("✓ Database connections closed")
