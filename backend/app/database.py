"""Database connection and session management with Neon DB"""
from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create synchronous engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False,
)

def create_db_and_tables():
    """Create all database tables"""
    SQLModel.metadata.create_all(engine)

async def init_db():
    """Initialize database (async wrapper for compatibility)"""
    create_db_and_tables()

def get_session():
    """Get a database session"""
    with Session(engine) as session:
        yield session
