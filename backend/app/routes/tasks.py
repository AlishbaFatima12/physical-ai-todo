"""
Task management API routes.

Provides RESTful endpoints for CRUD operations on tasks.
"""

import json
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.database import get_session
from app.schemas import TaskCreate, TaskUpdate, TaskPatch, TaskRead, TaskListResponse

router = APIRouter(prefix="/api/v1/tasks", tags=["tasks"])


@router.get("", response_model=TaskListResponse)
async def get_tasks(
    limit: int = Query(50, ge=1, le=100, description="Maximum tasks per page"),
    offset: int = Query(0, ge=0, description="Number of tasks to skip"),
    search: Optional[str] = Query(None, description="Search in title/description"),
    completed: Optional[bool] = Query(None, description="Filter by completion status"),
    priority: Optional[str] = Query(None, pattern="^(high|medium|low)$", description="Filter by priority"),
    tags: Optional[str] = Query(None, description="Comma-separated tags to filter by"),
    sort: str = Query("created_at", pattern="^(created_at|updated_at|priority|title)$", description="Sort field"),
    order: str = Query("desc", pattern="^(asc|desc)$", description="Sort order"),
    session: AsyncSession = Depends(get_session),
):
    """
    List all tasks with optional filtering, search, sorting, and pagination.

    **Query Parameters:**
    - **limit**: Max tasks per page (1-100, default: 50)
    - **offset**: Number of tasks to skip (default: 0)
    - **search**: Search term for title/description
    - **completed**: Filter by completion (true/false)
    - **priority**: Filter by priority (high/medium/low)
    - **tags**: Comma-separated tags (e.g., "work,urgent")
    - **sort**: Sort by field (created_at/updated_at/priority/title)
    - **order**: Sort order (asc/desc)

    **Returns:**
    - List of tasks matching filters
    - Total count of matching tasks
    - Pagination info (limit, offset)
    """
    tasks, total = await crud.list_tasks(
        session=session,
        limit=limit,
        offset=offset,
        search=search,
        completed=completed,
        priority=priority,
        tags=tags,
        sort=sort,
        order=order,
    )

    # Convert tags from JSON string to list for each task
    tasks_with_parsed_tags = []
    for task in tasks:
        task_dict = {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
            "priority": task.priority,
            "tags": json.loads(task.tags) if task.tags else [],
            "created_at": task.created_at,
            "updated_at": task.updated_at,
        }
        tasks_with_parsed_tags.append(TaskRead(**task_dict))

    return TaskListResponse(tasks=tasks_with_parsed_tags, total=total, limit=limit, offset=offset)


@router.post("", response_model=TaskRead, status_code=201)
async def create_task(
    task_data: TaskCreate,
    session: AsyncSession = Depends(get_session),
):
    """
    Create a new task.

    **Request Body:**
    - **title**: Task title (required, 1-200 chars)
    - **description**: Task description (optional, max 2000 chars)
    - **priority**: Priority level (high/medium/low, default: medium)
    - **tags**: Array of tag strings (default: [])

    **Returns:**
    - Created task with ID and timestamps
    """
    db_task = await crud.create_task(task_data, session)

    # Parse tags from JSON string
    return TaskRead(
        id=db_task.id,
        title=db_task.title,
        description=db_task.description,
        completed=db_task.completed,
        priority=db_task.priority,
        tags=json.loads(db_task.tags) if db_task.tags else [],
        created_at=db_task.created_at,
        updated_at=db_task.updated_at,
    )


@router.get("/{task_id}", response_model=TaskRead)
async def get_task(
    task_id: int,
    session: AsyncSession = Depends(get_session),
):
    """
    Get a single task by ID.

    **Path Parameters:**
    - **task_id**: Task ID to retrieve

    **Returns:**
    - Task details

    **Raises:**
    - 404: Task not found
    """
    db_task = await crud.get_task(task_id, session)
    if not db_task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")

    return TaskRead(
        id=db_task.id,
        title=db_task.title,
        description=db_task.description,
        completed=db_task.completed,
        priority=db_task.priority,
        tags=json.loads(db_task.tags) if db_task.tags else [],
        created_at=db_task.created_at,
        updated_at=db_task.updated_at,
    )


@router.put("/{task_id}", response_model=TaskRead)
async def update_task(
    task_id: int,
    task_data: TaskUpdate,
    session: AsyncSession = Depends(get_session),
):
    """
    Update a task (full replacement).

    **Path Parameters:**
    - **task_id**: Task ID to update

    **Request Body:**
    - All task fields (title, description, priority, tags, completed)

    **Returns:**
    - Updated task

    **Raises:**
    - 404: Task not found
    """
    db_task = await crud.update_task(task_id, task_data, session)
    if not db_task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")

    return TaskRead(
        id=db_task.id,
        title=db_task.title,
        description=db_task.description,
        completed=db_task.completed,
        priority=db_task.priority,
        tags=json.loads(db_task.tags) if db_task.tags else [],
        created_at=db_task.created_at,
        updated_at=db_task.updated_at,
    )


@router.patch("/{task_id}", response_model=TaskRead)
async def patch_task(
    task_id: int,
    task_data: TaskPatch,
    session: AsyncSession = Depends(get_session),
):
    """
    Partially update a task.

    **Path Parameters:**
    - **task_id**: Task ID to update

    **Request Body:**
    - Only the fields you want to update (all optional)

    **Example:**
    ```json
    {"completed": true}
    ```

    **Returns:**
    - Updated task

    **Raises:**
    - 404: Task not found
    """
    db_task = await crud.patch_task(task_id, task_data, session)
    if not db_task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")

    return TaskRead(
        id=db_task.id,
        title=db_task.title,
        description=db_task.description,
        completed=db_task.completed,
        priority=db_task.priority,
        tags=json.loads(db_task.tags) if db_task.tags else [],
        created_at=db_task.created_at,
        updated_at=db_task.updated_at,
    )


@router.delete("/{task_id}", status_code=204)
async def delete_task(
    task_id: int,
    session: AsyncSession = Depends(get_session),
):
    """
    Delete a task.

    **Path Parameters:**
    - **task_id**: Task ID to delete

    **Returns:**
    - No content (204)

    **Raises:**
    - 404: Task not found
    """
    deleted = await crud.delete_task(task_id, session)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")

    return None


@router.post("/{task_id}/toggle", response_model=TaskRead)
async def toggle_task_completion(
    task_id: int,
    session: AsyncSession = Depends(get_session),
):
    """
    Toggle task completion status (completed <-> not completed).

    **Path Parameters:**
    - **task_id**: Task ID to toggle

    **Returns:**
    - Updated task with toggled completion status

    **Raises:**
    - 404: Task not found
    """
    db_task = await crud.toggle_complete(task_id, session)
    if not db_task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")

    return TaskRead(
        id=db_task.id,
        title=db_task.title,
        description=db_task.description,
        completed=db_task.completed,
        priority=db_task.priority,
        tags=json.loads(db_task.tags) if db_task.tags else [],
        created_at=db_task.created_at,
        updated_at=db_task.updated_at,
    )
