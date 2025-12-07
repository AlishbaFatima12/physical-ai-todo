"""
Physical AI Todo Application - FastAPI Backend

Main application entry point with CORS, routes, and lifecycle management.
"""

import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db, close_db
from app.routes import tasks

# Load environment variables
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.

    Handles startup and shutdown events:
    - Startup: Initialize database tables
    - Shutdown: Close database connections
    """
    # Startup
    print("Starting up Physical AI Todo API...")
    try:
        await init_db()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Warning: Database initialization failed: {e}")

    yield

    # Shutdown
    print("Shutting down...")
    await close_db()
    print("Database connections closed")


# Create FastAPI app
app = FastAPI(
    title="Physical AI Todo API",
    description="RESTful API for managing tasks with priorities, tags, and AI features",
    version="2.0.0",
    lifespan=lifespan,
)


# Configure CORS
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register routes
app.include_router(tasks.router)


@app.get("/", tags=["health"])
async def root():
    """
    Root endpoint - API health check.

    Returns:
        Welcome message and API status
    """
    return {
        "message": "Physical AI Todo API",
        "version": "2.0.0",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health", tags=["health"])
async def health_check():
    """
    Health check endpoint for monitoring.

    Returns:
        Health status
    """
    return {"status": "healthy", "service": "physical-ai-todo-api"}


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info",
    )
