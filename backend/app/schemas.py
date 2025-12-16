"""Pydantic schemas for request/response validation"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from app.models import Priority, ActionType


# Task schemas
class TaskBase(BaseModel):
    """Base task schema"""
    title: str = Field(..., max_length=500)
    description: Optional[str] = Field(None, max_length=5000)
    priority: Priority = Priority.MEDIUM
    tags: Optional[List[str]] = []

    # Phase V: Due Dates & Reminders
    due_date: Optional[datetime] = None
    reminder_time: Optional[datetime] = None

    # Phase V: Recurring Tasks
    is_recurring: bool = False
    recurrence_pattern: Optional[str] = Field(None, max_length=50)  # daily, weekly, monthly
    recurrence_end_date: Optional[datetime] = None


class TaskCreate(TaskBase):
    """Schema for creating a task"""
    display_order: Optional[int] = 0


class TaskUpdate(BaseModel):
    """Schema for updating a task"""
    title: Optional[str] = Field(None, max_length=500)
    description: Optional[str] = Field(None, max_length=5000)
    completed: Optional[bool] = None
    priority: Optional[Priority] = None
    tags: Optional[List[str]] = None
    display_order: Optional[int] = None

    # Phase V: Due Dates & Reminders
    due_date: Optional[datetime] = None
    reminder_time: Optional[datetime] = None

    # Phase V: Recurring Tasks
    is_recurring: Optional[bool] = None
    recurrence_pattern: Optional[str] = None
    recurrence_end_date: Optional[datetime] = None


class TaskPatch(BaseModel):
    """Schema for partially updating a task (PATCH)"""
    title: Optional[str] = Field(None, max_length=500)
    description: Optional[str] = Field(None, max_length=5000)
    completed: Optional[bool] = None
    priority: Optional[Priority] = None
    tags: Optional[List[str]] = None
    display_order: Optional[int] = None

    # Phase V: Due Dates & Reminders
    due_date: Optional[datetime] = None
    reminder_time: Optional[datetime] = None

    # Phase V: Recurring Tasks
    is_recurring: Optional[bool] = None
    recurrence_pattern: Optional[str] = None
    recurrence_end_date: Optional[datetime] = None


class SubtaskResponse(BaseModel):
    """Subtask response schema"""
    id: int
    task_id: int
    title: str
    completed: bool
    display_order: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NoteResponse(BaseModel):
    """Note response schema"""
    id: int
    task_id: int
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AttachmentResponse(BaseModel):
    """Attachment response schema"""
    id: int
    task_id: int
    filename: str
    file_url: str
    file_size: int
    mime_type: str
    ocr_text: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class ActivityLogResponse(BaseModel):
    """Activity log response schema"""
    id: int
    task_id: int
    action_type: ActionType
    field_changed: Optional[str]
    old_value: Optional[str]
    new_value: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class TaskResponse(TaskBase):
    """Task response schema with optional relations"""
    id: int
    completed: bool
    display_order: int
    is_template: bool
    created_at: datetime
    updated_at: datetime
    subtasks: Optional[List[SubtaskResponse]] = None
    notes: Optional[List[NoteResponse]] = None
    attachments: Optional[List[AttachmentResponse]] = None
    activity_logs: Optional[List[ActivityLogResponse]] = None

    class Config:
        from_attributes = True


class TaskRead(BaseModel):
    """Task read schema for API responses"""
    id: int
    title: str
    description: Optional[str]
    completed: bool
    priority: Priority
    tags: List[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TaskListResponse(BaseModel):
    """Task list response with pagination"""
    tasks: List[TaskRead]
    total: int
    limit: int
    offset: int


# Subtask schemas
class SubtaskCreate(BaseModel):
    """Schema for creating a subtask"""
    title: str = Field(..., max_length=500)
    display_order: Optional[int] = 0


class SubtaskUpdate(BaseModel):
    """Schema for updating a subtask"""
    title: Optional[str] = Field(None, max_length=500)
    completed: Optional[bool] = None
    display_order: Optional[int] = None


# Note schemas
class NoteCreate(BaseModel):
    """Schema for creating a note"""
    content: str = Field(..., max_length=5000)


class NoteUpdate(BaseModel):
    """Schema for updating a note"""
    content: str = Field(..., max_length=5000)


# Attachment schemas
class AttachmentCreate(BaseModel):
    """Schema for creating an attachment"""
    filename: str
    file_url: str
    file_size: int
    mime_type: str


# Template schemas
class TemplateCreate(BaseModel):
    """Schema for creating a template"""
    name: str = Field(..., max_length=200)
    title: str = Field(..., max_length=500)
    description: Optional[str] = Field(None, max_length=5000)
    priority: Priority = Priority.MEDIUM
    tags: Optional[str] = Field(None, max_length=1000)
    subtasks: Optional[str] = Field(None, max_length=10000)


class TemplateResponse(TemplateCreate):
    """Template response schema"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Bulk operation schemas
class BulkOperationRequest(BaseModel):
    """Schema for bulk operations"""
    task_ids: List[int]


class BulkTagRequest(BulkOperationRequest):
    """Schema for bulk tag operation"""
    tag: str


class BulkPriorityRequest(BulkOperationRequest):
    """Schema for bulk priority operation"""
    priority: Priority


# Reorder schema
class ReorderRequest(BaseModel):
    """Schema for reordering tasks/subtasks"""
    items: List[dict]  # [{"id": 1, "display_order": 0}, ...]
