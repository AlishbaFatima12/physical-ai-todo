"""
SQLModel database table definitions.

These models map directly to database tables and define the schema.
"""

from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Task(SQLModel, table=True):
    """
    Task table for storing todo items with priorities, tags, and completion status.

    Schema matches Phase II requirements with support for:
    - Basic CRUD operations
    - Priorities (high, medium, low)
    - Tags (multiple tags per task)
    - Search and filtering
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=200, index=True, nullable=False)
    description: str = Field(default="", max_length=2000)
    completed: bool = Field(default=False, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    # Phase II New Fields
    priority: str = Field(default="medium", max_length=10, index=True)
    tags: str = Field(default="[]", max_length=500)  # JSON array as string
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    class Config:
        """SQLModel configuration"""

        schema_extra = {
            "example": {
                "id": 1,
                "title": "Buy groceries",
                "description": "Milk, eggs, bread",
                "completed": False,
                "priority": "high",
                "tags": '["shopping", "urgent"]',
                "created_at": "2025-12-07T10:00:00Z",
                "updated_at": "2025-12-07T10:00:00Z",
            }
        }


class VoiceCommand(SQLModel, table=True):
    """
    Voice command table for storing voice interaction history.

    Tracks voice commands for analytics and debugging.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    transcript: str = Field(max_length=500, nullable=False)
    language: str = Field(max_length=5, nullable=False)  # en, ur, ar, es, fr, de
    action: str = Field(max_length=50)  # create_task, complete_task, etc.
    success: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    class Config:
        """SQLModel configuration"""

        schema_extra = {
            "example": {
                "id": 1,
                "transcript": "Add task buy milk",
                "language": "en",
                "action": "create_task",
                "success": True,
                "created_at": "2025-12-07T10:00:00Z",
            }
        }


class ChatMessage(SQLModel, table=True):
    """
    Chat message table for storing AI chatbot conversation history.

    Stores both user and assistant messages for context preservation.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    role: str = Field(max_length=10, nullable=False)  # user or assistant
    content: str = Field(max_length=5000, nullable=False)
    language: str = Field(max_length=5, nullable=False)  # en, ur, ar, es, fr, de
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    class Config:
        """SQLModel configuration"""

        schema_extra = {
            "example": {
                "id": 1,
                "role": "user",
                "content": "What tasks do I have?",
                "language": "en",
                "created_at": "2025-12-07T10:00:00Z",
            }
        }
