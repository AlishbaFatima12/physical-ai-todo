"""
MCP Tool Functions for Phase III AI Chatbot

Implements the actual tool functions that the AI agent can call.
Each tool wraps existing CRUD operations with proper validation
and error handling.

These tools are stateless and operate directly on the database
using the existing CRUD functions from app.crud.
"""

import json
from typing import Dict, Any, List
from sqlmodel import Session

from app.crud import (
    create_task,
    list_tasks,
    get_task,
    patch_task,
    delete_task as crud_delete_task
)
from app.schemas import TaskCreate, TaskPatch
from app.mcp.schemas import (
    AddTaskSchema,
    ListTasksSchema,
    CompleteTaskSchema,
    DeleteTaskSchema,
    UpdateTaskSchema
)


def add_task(params: AddTaskSchema, session: Session) -> Dict[str, Any]:
    """
    MCP Tool: Add a new task to the user's todo list.

    Args:
        params: AddTaskSchema with user_id, title, description, priority
        session: Database session

    Returns:
        Dict with success status and created task details
    """
    try:
        # Create task using existing CRUD function
        task_data = TaskCreate(
            title=params.title,
            description=params.description,
            priority=params.priority,
            tags=[]  # Empty tags for now
        )

        task = create_task(task_data, session, params.user_id)

        return {
            "success": True,
            "task_id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "message": f"Task '{task.title}' created successfully with ID {task.id}"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Failed to create task: {str(e)}"
        }


def list_tasks_tool(params: ListTasksSchema, session: Session) -> Dict[str, Any]:
    """
    MCP Tool: List user's tasks with optional filtering.

    Args:
        params: ListTasksSchema with user_id, status, priority, limit
        session: Database session

    Returns:
        Dict with success status and list of tasks
    """
    try:
        # Determine completed filter based on status
        completed_filter = None
        if params.status == "pending":
            completed_filter = False
        elif params.status == "completed":
            completed_filter = True

        # Get tasks using existing CRUD function
        tasks, total = list_tasks(
            session=session,
            user_id=params.user_id,
            limit=params.limit,
            completed=completed_filter,
            priority=params.priority
        )

        # Format tasks for response
        task_list = []
        for task in tasks:
            task_dict = {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "priority": task.priority,
                "completed": task.completed,
                "created_at": task.created_at.isoformat() if task.created_at else None
            }
            task_list.append(task_dict)

        return {
            "success": True,
            "tasks": task_list,
            "total": total,
            "count": len(task_list),
            "message": f"Found {len(task_list)} {params.status} task(s)"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "tasks": [],
            "message": f"Failed to list tasks: {str(e)}"
        }


def complete_task_tool(params: CompleteTaskSchema, session: Session) -> Dict[str, Any]:
    """
    MCP Tool: Mark a task as complete.

    Args:
        params: CompleteTaskSchema with user_id, task_id
        session: Database session

    Returns:
        Dict with success status and updated task details
    """
    try:
        # Verify task exists and belongs to user
        task = get_task(params.task_id, session)
        if not task:
            return {
                "success": False,
                "error": "Task not found",
                "message": f"Task with ID {params.task_id} not found"
            }

        if task.user_id != params.user_id:
            return {
                "success": False,
                "error": "Permission denied",
                "message": "You don't have permission to complete this task"
            }

        # Mark as complete
        task_patch = TaskPatch(completed=True)
        updated_task = patch_task(params.task_id, task_patch, session)

        return {
            "success": True,
            "task_id": updated_task.id,
            "title": updated_task.title,
            "completed": updated_task.completed,
            "message": f"Task '{updated_task.title}' marked as complete"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Failed to complete task: {str(e)}"
        }


def delete_task_tool(params: DeleteTaskSchema, session: Session) -> Dict[str, Any]:
    """
    MCP Tool: Delete a task from the user's todo list.

    Args:
        params: DeleteTaskSchema with user_id, task_id
        session: Database session

    Returns:
        Dict with success status
    """
    try:
        # Verify task exists and belongs to user
        task = get_task(params.task_id, session)
        if not task:
            return {
                "success": False,
                "error": "Task not found",
                "message": f"Task with ID {params.task_id} not found"
            }

        if task.user_id != params.user_id:
            return {
                "success": False,
                "error": "Permission denied",
                "message": "You don't have permission to delete this task"
            }

        # Store title before deletion
        task_title = task.title

        # Delete task
        deleted = crud_delete_task(params.task_id, session)

        if deleted:
            return {
                "success": True,
                "task_id": params.task_id,
                "message": f"Task '{task_title}' deleted successfully"
            }
        else:
            return {
                "success": False,
                "error": "Deletion failed",
                "message": "Failed to delete task"
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Failed to delete task: {str(e)}"
        }


def update_task_tool(params: UpdateTaskSchema, session: Session) -> Dict[str, Any]:
    """
    MCP Tool: Update task details (title, description, priority).

    Args:
        params: UpdateTaskSchema with user_id, task_id, and optional fields
        session: Database session

    Returns:
        Dict with success status and updated task details
    """
    try:
        # Verify task exists and belongs to user
        task = get_task(params.task_id, session)
        if not task:
            return {
                "success": False,
                "error": "Task not found",
                "message": f"Task with ID {params.task_id} not found"
            }

        if task.user_id != params.user_id:
            return {
                "success": False,
                "error": "Permission denied",
                "message": "You don't have permission to update this task"
            }

        # Build patch data from provided fields
        update_data = {}
        if params.title is not None:
            update_data["title"] = params.title
        if params.description is not None:
            update_data["description"] = params.description
        if params.priority is not None:
            update_data["priority"] = params.priority

        if not update_data:
            return {
                "success": False,
                "error": "No updates provided",
                "message": "No fields to update"
            }

        # Update task
        task_patch = TaskPatch(**update_data)
        updated_task = patch_task(params.task_id, task_patch, session)

        return {
            "success": True,
            "task_id": updated_task.id,
            "title": updated_task.title,
            "description": updated_task.description,
            "priority": updated_task.priority,
            "message": f"Task '{updated_task.title}' updated successfully"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Failed to update task: {str(e)}"
        }


# Tool registry for OpenAI function calling
TOOLS = {
    "add_task": {
        "function": add_task,
        "schema": AddTaskSchema,
        "description": "Add a new task to the user's todo list",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {"type": "integer", "description": "ID of the user"},
                "title": {"type": "string", "description": "Task title"},
                "description": {"type": "string", "description": "Task description"},
                "priority": {"type": "string", "enum": ["low", "medium", "high"], "description": "Priority level"}
            },
            "required": ["user_id", "title"]
        }
    },
    "list_tasks": {
        "function": list_tasks_tool,
        "schema": ListTasksSchema,
        "description": "List user's tasks with optional filtering by status and priority",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {"type": "integer", "description": "ID of the user"},
                "status": {"type": "string", "enum": ["all", "pending", "completed"], "description": "Filter by status"},
                "priority": {"type": "string", "enum": ["low", "medium", "high"], "description": "Filter by priority"},
                "limit": {"type": "integer", "description": "Maximum number of tasks"}
            },
            "required": ["user_id"]
        }
    },
    "complete_task": {
        "function": complete_task_tool,
        "schema": CompleteTaskSchema,
        "description": "Mark a task as complete",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {"type": "integer", "description": "ID of the user"},
                "task_id": {"type": "integer", "description": "ID of the task to complete"}
            },
            "required": ["user_id", "task_id"]
        }
    },
    "delete_task": {
        "function": delete_task_tool,
        "schema": DeleteTaskSchema,
        "description": "Delete a task from the user's todo list",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {"type": "integer", "description": "ID of the user"},
                "task_id": {"type": "integer", "description": "ID of the task to delete"}
            },
            "required": ["user_id", "task_id"]
        }
    },
    "update_task": {
        "function": update_task_tool,
        "schema": UpdateTaskSchema,
        "description": "Update task details (title, description, priority)",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {"type": "integer", "description": "ID of the user"},
                "task_id": {"type": "integer", "description": "ID of the task to update"},
                "title": {"type": "string", "description": "New task title"},
                "description": {"type": "string", "description": "New task description"},
                "priority": {"type": "string", "enum": ["low", "medium", "high"], "description": "New priority"}
            },
            "required": ["user_id", "task_id"]
        }
    }
}
