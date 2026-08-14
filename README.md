# Todo CLI v3.0

Feature-rich terminal todo manager in Python.

## What's new in v3.0
- Recurring tasks (daily / weekly / monthly) with streak counter
- Per-task notes with timestamps
- Daily report (print or save to file)
- Bulk complete multiple tasks at once
- Progress bar in stats
- Due-today / overdue / soon warnings inline in list
- Archive completed tasks to archive.json
- App config centralized in config.py

## Modules
| File           | Purpose                        |
|----------------|--------------------------------|
| todo.py        | Main app and CLI               |
| recur.py       | Recurring task scheduling      |
| notes.py       | Per-task notes                 |
| report.py      | Daily summary report           |
| progressbar.py | Unicode progress bar           |
| config.py      | App-wide settings              |

## Run

python todo.py


## Commands
| Command      | Action                          |
|--------------|---------------------------------|
| add          | Add task (with repeat option)   |
| list         | List all tasks                  |
| pending      | Pending tasks only              |
| done         | Mark task complete              |
| bulk         | Complete multiple tasks         |
| del          | Delete task                     |
| edit         | Edit task fields                |
| undo         | Undo last action                |
| search       | Search by keyword or tag        |
| tag          | Filter by tag                   |
| pri          | Filter by priority              |
| sort         | Sort by priority/due/title      |
| overdue      | Show overdue tasks              |
| note         | Add or view notes on a task     |
| stats        | Statistics with progress bar    |
| report       | Daily summary report            |
| archive      | Archive all completed tasks     |
| archive-view | Browse archived tasks           |
| save         | Save tasks to file              |
| export       | Export JSON with metadata       |
| quit         | Save and exit                   |
