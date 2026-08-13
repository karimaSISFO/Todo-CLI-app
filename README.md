# Todo CLI v2.0

Upgraded command-line todo manager in Python.

## What's new in v2.0
- Due dates per task (YYYY-MM-DD)
- Tags support (#work, #personal, etc)
- Colorized terminal output (ANSI)
- Export to JSON with metadata
- Undo last action (add / complete / delete)
- Overdue detection on startup
- Filter by tag or priority
- Sort by priority, due date, or title
- Edit tasks in place

## Run

python todo.py


## Commands
| Command  | Action                        |
|----------|-------------------------------|
| add      | Add a new task                |
| list     | List all tasks                |
| pending  | List only pending tasks       |
| done     | Mark a task complete          |
| del      | Delete a task                 |
| edit     | Edit task fields              |
| undo     | Undo last action              |
| search   | Search by keyword or tag      |
| tag      | Filter by tag                 |
| pri      | Filter by priority            |
| sort     | Sort by priority / due /title |
| overdue  | Show overdue tasks            |
| stats    | Show statistics               |
| save     | Save tasks to file            |
| export   | Export to JSON                |
| quit     | Save and exit                 |
