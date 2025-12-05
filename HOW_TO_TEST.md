# How to Test the Todo App

## Location
Your project is at: `C:\Users\Ahsan\physical-ai-todo`

## Method 1: Quick CLI Testing (Separate Commands)

### Open PowerShell or CMD and navigate to project:
```bash
cd C:\Users\Ahsan\physical-ai-todo
```

### Try these commands one by one:

#### 1. Add a task:
```bash
python -m src.todo.app add "Buy groceries" -d "Milk, eggs, bread"
```

#### 2. Add more tasks:
```bash
python -m src.todo.app add "Call dentist"
python -m src.todo.app add "Finish report" -d "Q4 summary"
```

#### 3. List tasks (will be empty - see note below):
```bash
python -m src.todo.app list
```

**Note**: Each command runs in a NEW process with FRESH memory. 
This is Phase I's in-memory design - data doesn't persist between commands.

#### 4. Get help:
```bash
python -m src.todo.app --help
python -m src.todo.app add --help
```

---

## Method 2: Interactive Python Session (Recommended!)

This keeps data in memory during your session.

### Open PowerShell/CMD:
```bash
cd C:\Users\Ahsan\physical-ai-todo
python
```

### Then paste this code:
```python
# Import the storage module
from src.todo import storage

# Add some tasks
print("Adding tasks...")
task1 = storage.add_task("Buy groceries", "Milk, eggs, bread, coffee")
task2 = storage.add_task("Call mom", "Discuss weekend plans")
task3 = storage.add_task("Write report")
print(f"Created {task1['id']}, {task2['id']}, {task3['id']}")

# List all tasks
print("\nAll tasks:")
tasks = storage.list_tasks()
for task in tasks:
    status = "[X]" if task['completed'] else "[ ]"
    print(f"  {status} [{task['id']}] {task['title']}")

# Mark one complete
print("\nMarking task 1 complete...")
storage.mark_complete(1, True)

# List again
print("\nAfter completion:")
tasks = storage.list_tasks()
for task in tasks:
    status = "[X]" if task['completed'] else "[ ]"
    print(f"  {status} [{task['id']}] {task['title']}")

# Update a task
print("\nUpdating task 3...")
updated = storage.update_task(3, title="Write Q4 Report", description="Financial summary")
print(f"Updated: {updated['title']}")

# Delete a task
print("\nDeleting task 2...")
storage.delete_task(2)

# Final list
print("\nFinal tasks:")
tasks = storage.list_tasks()
for task in tasks:
    status = "[X]" if task['completed'] else "[ ]"
    desc = f" - {task['description']}" if task['description'] else ""
    print(f"  {status} [{task['id']}] {task['title']}{desc}")

print(f"\nTotal: {len(tasks)} tasks")
```

---

## Method 3: Run the Test Script

### Quick automated test:
```bash
cd C:\Users\Ahsan\physical-ai-todo
bash test_session.sh
```

Or on Windows without bash:
```bash
python -c "exec(open('test_session.sh').read().replace('#!/bin/bash','').replace('echo','print'))"
```

---

## Method 4: Run the Test Suite

### See all 19 tests pass:
```bash
cd C:\Users\Ahsan\physical-ai-todo
python -m unittest discover tests -v
```

**Output**: Should show 19/19 tests passing!

---

## Method 5: Create a Python Script

### Create `my_test.py`:
```python
from src.todo import storage

# Your custom testing here
print("My Todo App Test")
print("-" * 40)

# Add tasks
storage.add_task("Task 1", "First task")
storage.add_task("Task 2", "Second task")
storage.add_task("Task 3", "Third task")

# List them
tasks = storage.list_tasks()
print(f"Created {len(tasks)} tasks:")
for t in tasks:
    print(f"  [{t['id']}] {t['title']}")

# Mark one complete
storage.mark_complete(1, True)
print("\nMarked task 1 complete!")

# List again
tasks = storage.list_tasks()
for t in tasks:
    status = "[X]" if t['completed'] else "[ ]"
    print(f"  {status} [{t['id']}] {t['title']}")
```

### Run it:
```bash
python my_test.py
```

---

## Custom Skills to Test With

### Check if everything is working correctly:
```bash
/check-constitution  # Verify Phase I compliance
/test-python        # Run tests with detailed analysis
```

---

## Quick Commands Reference

| Command | What It Does |
|---------|-------------|
| `python -m src.todo.app add "title"` | Add a task |
| `python -m src.todo.app add "title" -d "desc"` | Add with description |
| `python -m src.todo.app list` | List all tasks |
| `python -m src.todo.app complete <id>` | Mark complete |
| `python -m src.todo.app update <id> -t "new"` | Update title |
| `python -m src.todo.app delete <id>` | Delete task |
| `python -m src.todo.app --help` | Show help |

---

## Understanding Phase I Behavior

**Important**: Phase I uses in-memory storage:

✅ **Within a Python session**: Data persists
```python
python
>>> from src.todo import storage
>>> storage.add_task("Task 1")
>>> storage.add_task("Task 2")
>>> storage.list_tasks()  # Returns 2 tasks ✅
```

❌ **Between CLI commands**: Data resets (new process each time)
```bash
python -m src.todo.app add "Task 1"   # Process 1
python -m src.todo.app add "Task 2"   # Process 2 (fresh memory)
python -m src.todo.app list           # Process 3 (empty) ❌
```

**This is expected Phase I behavior!**
- Phase II will add database persistence
- Then CLI commands will persist data between runs

---

## Need Help?

- Check README.md for full documentation
- Run `/test-python` to see test results
- Run `/check-constitution` to verify everything is correct

---

## File Locations

```
C:\Users\Ahsan\physical-ai-todo\
├── src/todo/          ← Source code here
│   ├── app.py         ← CLI interface
│   ├── storage.py     ← CRUD operations  
│   └── models.py      ← Validation
├── tests/             ← Tests here
│   ├── test_storage.py
│   └── test_cli.py
├── README.md          ← Full documentation
└── test_session.sh    ← Automated test script
```
