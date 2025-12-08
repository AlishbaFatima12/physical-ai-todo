"""SQLModel database models for Physical AI Todo"""
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from enum import Enum


class Priority(str, Enum):
    """Task priority levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ActionType(str, Enum):
    """Activity log action types"""
    CREATED = "created"
    UPDATED = "updated"
    COMPLETED = "completed"
    DELETED = "deleted"
    RESTORED = "restored"


class Task(SQLModel, table=True):
    """Main task model"""
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, max_length=500)
    description: Optional[str] = Field(default=None, max_length=5000)
    completed: bool = Field(default=False, index=True)
    priority: Priority = Field(default=Priority.MEDIUM, index=True)
    tags: Optional[str] = Field(default=None, max_length=1000)  # Comma-separated tags
    display_order: int = Field(default=0, index=True)
    is_template: bool = Field(default=False, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships
    subtasks: List["Subtask"] = Relationship(back_populates="task", cascade_delete=True)
    notes: List["Note"] = Relationship(back_populates="task", cascade_delete=True)
    attachments: List["Attachment"] = Relationship(back_populates="task", cascade_delete=True)
    activity_logs: List["ActivityLog"] = Relationship(back_populates="task", cascade_delete=True)


class Subtask(SQLModel, table=True):
    """Subtask model for task checklists"""
    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: int = Field(foreign_key="task.id", index=True)
    title: str = Field(max_length=500)
    completed: bool = Field(default=False)
    display_order: int = Field(default=0, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships
    task: Optional[Task] = Relationship(back_populates="subtasks")


class Note(SQLModel, table=True):
    """Note model for task notes"""
    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: int = Field(foreign_key="task.id", index=True)
    content: str = Field(max_length=5000)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships
    task: Optional[Task] = Relationship(back_populates="notes")


class Attachment(SQLModel, table=True):
    """Attachment model for task file attachments"""
    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: int = Field(foreign_key="task.id", index=True)
    filename: str = Field(max_length=255)
    file_url: str = Field(max_length=1000)
    file_size: int = Field(default=0)  # Size in bytes
    mime_type: str = Field(max_length=100)
    ocr_text: Optional[str] = Field(default=None, max_length=10000)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    
    # Relationships
    task: Optional[Task] = Relationship(back_populates="attachments")


class Template(SQLModel, table=True):
    """Template model for task templates"""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=200)
    title: str = Field(max_length=500)
    description: Optional[str] = Field(default=None, max_length=5000)
    priority: Priority = Field(default=Priority.MEDIUM)
    tags: Optional[str] = Field(default=None, max_length=1000)
    subtasks: Optional[str] = Field(default=None, max_length=10000)  # JSON array of subtask titles
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ActivityLog(SQLModel, table=True):
    """Activity log model for tracking task changes"""
    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: int = Field(foreign_key="task.id", index=True)
    action_type: ActionType = Field(index=True)
    field_changed: Optional[str] = Field(default=None, max_length=100)
    old_value: Optional[str] = Field(default=None, max_length=1000)
    new_value: Optional[str] = Field(default=None, max_length=1000)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    
    # Relationships
    task: Optional[Task] = Relationship(back_populates="activity_logs")


class VoiceCommand(SQLModel, table=True):
    """Voice command model for tracking voice interactions"""
    id: Optional[int] = Field(default=None, primary_key=True)
    transcript: str = Field(max_length=2000)
    language: str = Field(max_length=10, index=True)  # en, ur, ar, es, fr, de
    intent: Optional[str] = Field(default=None, max_length=100)  # create, update, delete, complete
    confidence: Optional[float] = Field(default=None)  # 0.0 to 1.0
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)


class ChatMessage(SQLModel, table=True):
    """Chat message model for AI chatbot conversations"""
    id: Optional[int] = Field(default=None, primary_key=True)
    role: str = Field(max_length=20)  # user, assistant
    content: str = Field(max_length=10000)
    language: str = Field(max_length=10, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
