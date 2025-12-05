# Physical AI Todo Application - Phase I

A Python console-based todo application with in-memory storage, implementing the 5 basic CRUD operations.

## Features

Phase I implements the following core operations:
- ✅ **Add Task** - Create new tasks with title and optional description
- ✅ **View Tasks** - Display all tasks in table format
- ✅ **Update Task** - Modify task title and/or description
- ✅ **Delete Task** - Permanently remove tasks
- ✅ **Mark Complete** - Toggle task completion status

## Requirements

- Python 3.13+
- Zero external dependencies (standard library only)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd physical-ai-todo
```

2. No dependencies to install! Uses Python standard library only.

## Usage

### Add a Task

```bash
python -m src.todo.app add "Buy groceries" --description "Milk, eggs, bread"
```

Short form:
```bash
python -m src.todo.app add "Call mom" -d "Discuss weekend plans"
```

### List All Tasks

```bash
python -m src.todo.app list
```

Output:
```
ID  Status  Title                Description
──  ──────  ───────────────────  ─────────────────
1   [ ]     Buy groceries        Milk, eggs, bread
2   [X]     Call mom             Discuss weekend plans
```

### Mark Task as Complete

```bash
python -m src.todo.app complete 1
```

Mark as incomplete:
```bash
python -m src.todo.app complete 1 --incomplete
```

### Update a Task

```bash
python -m src.todo.app update 1 --title "Buy groceries and fruits"
```

Update description:
```bash
python -m src.todo.app update 1 --description "Milk, eggs, bread, apples"
```

Update both:
```bash
python -m src.todo.app update 1 -t "New title" -d "New description"
```

### Delete a Task

```bash
python -m src.todo.app delete 1
```

### Get Help

```bash
python -m src.todo.app --help
python -m src.todo.app add --help
```

## Architecture

```
src/
└── todo/
    ├── models.py     # Validation functions
    ├── storage.py    # In-memory CRUD operations
    └── app.py        # CLI interface

tests/
├── test_storage.py   # Unit tests (13 tests)
└── test_cli.py       # Integration tests (7 tests)
```

## Phase I Limitations

This is Phase I - in-memory storage only:
- Data is lost when program exits (no persistence)
- Single user only
- No search, filter, or sort (coming in Phase II)
- No priorities or tags (coming in Phase II)

## Testing

Run all tests:
```bash
python -m unittest discover tests
```

**Test Coverage**: 19/19 tests passing (100%)

## Data Model

Each task contains:
- `id` - Auto-generated, sequential, never reused
- `title` - Required, 1-200 characters
- `description` - Optional, max 2000 characters
- `completed` - Default: false
- `created_at` - ISO 8601 timestamp

## Evolution to Phase II

Phase II will add:
- Postgres database persistence
- FastAPI REST API
- Next.js web frontend
- User authentication
- Priorities, tags, search, filter, sort

## License

[Add your license here]
