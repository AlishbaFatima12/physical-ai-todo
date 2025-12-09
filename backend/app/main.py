"""FastAPI application entry point with CORS middleware and health check"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
from app.routes import tasks
from app.auth import routes as auth
from app.database import init_db

# Load environment variables
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan events for startup and shutdown"""
    # Startup
    print("Starting Physical AI Todo API")
    print("Initializing database...")
    await init_db()
    print("Database initialized successfully")
    yield
    # Shutdown
    print("Shutting down Physical AI Todo API")

# Initialize FastAPI app
app = FastAPI(
    title="Physical AI Todo API",
    description="Full-stack todo application with AI-powered features",
    version="0.1.0",
    lifespan=lifespan
)

# Configure CORS - allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://localhost:\d+",  # Allow any localhost port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Include routers
app.include_router(auth.router)  # Auth routes (public)
app.include_router(tasks.router)  # Task routes (protected)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "0.1.0",
        "service": "Physical AI Todo API"
    }

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "Physical AI Todo API",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
