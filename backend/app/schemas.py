"""
Pydantic schemas for request/response validation.

These schemas define the API contract and validate incoming/outgoing data.
Separate from SQLModel database models for flexibility.
"""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator


class TaskCreate(BaseModel):
    """Schema for creating a new task (POST /tasks)"""

    title: str = Field(..., min_length=1, max_length=200, description="Task title")
    description: str = Field(default="", max_length=2000, description="Task description")
    priority: str = Field(default="medium", pattern="^(high|medium|low)$", description="Priority level")
    tags: List[str] = Field(default=[], description="List of tags")

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v: str) -> str:
        """Validate title is not empty or whitespace only"""
        if not v or not v.strip():
            raise ValueError("Title cannot be empty")
        return v.strip()

    @field_validator("priority")
    @classmethod
    def validate_priority(cls, v: str) -> str:
        """Validate priority is one of allowed values"""
        if v not in ["high", "medium", "low"]:
            raise ValueError("Priority must be 'high', 'medium', or 'low'")
        return v

    class Config:
        """Pydantic configuration"""

        json_schema_extra = {
            "example": {
                "title": "Buy groceries",
                "description": "Milk, eggs, bread",
                "priority": "high",
                "tags": ["shopping", "urgent"],
            }
        }


class TaskUpdate(BaseModel):
    """Schema for full task update (PUT /tasks/{id})"""

    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., max_length=2000)
    priority: str = Field(..., pattern="^(high|medium|low)$")
    tags: List[str] = Field(...)
    completed: bool = Field(...)

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Title cannot be empty")
        return v.strip()

    class Config:
        """Pydantic configuration"""

        json_schema_extra = {
            "example": {
                "title": "Buy groceries and fruits",
                "description": "Milk, eggs, bread, apples",
                "priority": "medium",
                "tags": ["shopping"],
                "completed": False,
            }
        }


class TaskPatch(BaseModel):
    """Schema for partial task update (PATCH /tasks/{id})"""

    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    priority: Optional[str] = Field(None, pattern="^(high|medium|low)$")
    tags: Optional[List[str]] = None
    completed: Optional[bool] = None

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and (not v or not v.strip()):
            raise ValueError("Title cannot be empty")
        return v.strip() if v else v

    class Config:
        """Pydantic configuration"""

        json_schema_extra = {"example": {"completed": True}}


class TaskRead(BaseModel):
    """Schema for task response (GET /tasks/{id})"""

    id: int
    title: str
    description: str
    completed: bool
    priority: str
    tags: List[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic configuration"""

        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Buy groceries",
                "description": "Milk, eggs, bread",
                "completed": False,
                "priority": "high",
                "tags": ["shopping", "urgent"],
                "created_at": "2025-12-07T10:00:00Z",
                "updated_at": "2025-12-07T10:00:00Z",
            }
        }


class TaskListResponse(BaseModel):
    """Schema for task list response (GET /tasks)"""

    tasks: List[TaskRead]
    total: int = Field(..., description="Total number of tasks matching filters")
    limit: int = Field(..., description="Maximum tasks per page")
    offset: int = Field(..., description="Number of tasks skipped")

    class Config:
        """Pydantic configuration"""

        json_schema_extra = {
            "example": {
                "tasks": [
                    {
                        "id": 1,
                        "title": "Buy groceries",
                        "description": "Milk, eggs, bread",
                        "completed": False,
                        "priority": "high",
                        "tags": ["shopping", "urgent"],
                        "created_at": "2025-12-07T10:00:00Z",
                        "updated_at": "2025-12-07T10:00:00Z",
                    }
                ],
                "total": 1,
                "limit": 50,
                "offset": 0,
            }
        }


class VoiceCommandCreate(BaseModel):
    """Schema for creating a voice command record"""

    transcript: str = Field(..., max_length=500)
    language: str = Field(..., pattern="^(en|ur|ar|es|fr|de)$")

    class Config:
        """Pydantic configuration"""

        json_schema_extra = {"example": {"transcript": "Add task buy milk", "language": "en"}}


class ChatMessageCreate(BaseModel):
    """Schema for creating a chat message"""

    content: str = Field(..., min_length=1, max_length=5000)
    language: str = Field(default="en", pattern="^(en|ur|ar|es|fr|de)$")

    class Config:
        """Pydantic configuration"""

        json_schema_extra = {"example": {"content": "What tasks do I have?", "language": "en"}}
