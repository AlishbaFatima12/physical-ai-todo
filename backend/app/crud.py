"""
CRUD operations for Task management.

Provides async database operations for creating, reading, updating, and deleting tasks.
"""

import json
from datetime import datetime
from typing import List, Optional, Tuple

from sqlalchemy import select, func, or_
from sqlmodel import Session, col

from app.models import Task
from app.schemas import TaskCreate, TaskUpdate, TaskPatch


def create_task(task_data: TaskCreate, session: Session) -> Task:
    """
    Create a new task in the database.

    Args:
        task_data: Task creation data (title, description, priority, tags)
        session: Async database session

    Returns:
        Created Task object with generated ID and timestamps
    """
    # Convert tags list to JSON string for storage
    tags_json = json.dumps(task_data.tags)

    # Create new task instance
    db_task = Task(
        title=task_data.title,
        description=task_data.description,
        priority=task_data.priority,
        tags=tags_json,
        completed=False,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


def list_tasks(
    session: Session,
    limit: int = 50,
    offset: int = 0,
    search: Optional[str] = None,
    completed: Optional[bool] = None,
    priority: Optional[str] = None,
    tags: Optional[str] = None,
    sort: str = "created_at",
    order: str = "desc",
) -> Tuple[List[Task], int]:
    """
    List tasks with optional filtering, sorting, and pagination.

    Args:
        session: Async database session
        limit: Maximum number of tasks to return (default: 50)
        offset: Number of tasks to skip (default: 0)
        search: Search term for title/description (optional)
        completed: Filter by completion status (optional)
        priority: Filter by priority level (optional)
        tags: Comma-separated tags to filter by (optional)
        sort: Field to sort by (created_at, updated_at, priority, title)
        order: Sort order (asc or desc)

    Returns:
        Tuple of (list of tasks, total count)
    """
    # Build base query
    query = select(Task)

    # Apply filters
    if search:
        search_pattern = f"%{search}%"
        query = query.where(
            or_(
                col(Task.title).ilike(search_pattern),
                col(Task.description).ilike(search_pattern),
            )
        )

    if completed is not None:
        query = query.where(Task.completed == completed)

    if priority:
        query = query.where(Task.priority == priority)

    if tags:
        # Filter by tags (simple contains check)
        tag_list = [tag.strip() for tag in tags.split(",")]
        for tag in tag_list:
            query = query.where(col(Task.tags).contains(f'"{tag}"'))

    # Get total count before pagination
    count_query = select(func.count()).select_from(query.subquery())
    result = session.execute(count_query)
    total = result.scalar_one()

    # Apply sorting
    sort_column = getattr(Task, sort, Task.created_at)
    if order == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    # Apply pagination
    query = query.limit(limit).offset(offset)

    # Execute query
    result = session.execute(query)
    tasks = result.scalars().all()

    return list(tasks), total


def get_task(task_id: int, session: Session) -> Optional[Task]:
    """
    Get a single task by ID.

    Args:
        task_id: Task ID to retrieve
        session: Async database session

    Returns:
        Task object if found, None otherwise
    """
    result = session.execute(select(Task).where(Task.id == task_id))
    return result.scalar_one_or_none()


def update_task(task_id: int, task_data: TaskUpdate, session: Session) -> Optional[Task]:
    """
    Update a task with full replacement (PUT).

    Args:
        task_id: Task ID to update
        task_data: Complete task data for replacement
        session: Async database session

    Returns:
        Updated Task object if found, None otherwise
    """
    db_task = get_task(task_id, session)
    if not db_task:
        return None

    # Update all fields
    db_task.title = task_data.title
    db_task.description = task_data.description
    db_task.priority = task_data.priority
    db_task.tags = json.dumps(task_data.tags)
    db_task.completed = task_data.completed
    db_task.updated_at = datetime.utcnow()

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


def patch_task(task_id: int, task_data: TaskPatch, session: Session) -> Optional[Task]:
    """
    Partially update a task (PATCH).

    Args:
        task_id: Task ID to update
        task_data: Partial task data (only provided fields will be updated)
        session: Async database session

    Returns:
        Updated Task object if found, None otherwise
    """
    db_task = get_task(task_id, session)
    if not db_task:
        return None

    # Update only provided fields
    update_data = task_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        if field == "tags" and value is not None:
            setattr(db_task, field, json.dumps(value))
        elif value is not None:
            setattr(db_task, field, value)

    db_task.updated_at = datetime.utcnow()

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


def delete_task(task_id: int, session: Session) -> bool:
    """
    Delete a task by ID.

    Args:
        task_id: Task ID to delete
        session: Async database session

    Returns:
        True if task was deleted, False if not found
    """
    db_task = get_task(task_id, session)
    if not db_task:
        return False

    session.delete(db_task)
    session.commit()

    return True


def toggle_complete(task_id: int, session: Session) -> Optional[Task]:
    """
    Toggle task completion status.

    Args:
        task_id: Task ID to toggle
        session: Async database session

    Returns:
        Updated Task object if found, None otherwise
    """
    db_task = get_task(task_id, session)
    if not db_task:
        return None

    db_task.completed = not db_task.completed
    db_task.updated_at = datetime.utcnow()

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task
