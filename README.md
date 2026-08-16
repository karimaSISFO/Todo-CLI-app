# Todo CLI v5.0

A fully-featured terminal productivity suite in Python.

## What's new in v5.0
- Interactive TUI with arrow key navigation (tui.py)
- Pomodoro focus timer (focus.py)
- Event hook system for auto-save (hooks.py)
- Desktop notifications on overdue (notification.py)
- Task templates: save and reuse task configs (template.py)
- Ranked search now scores notes content (search.py)
- Streak analytics and leaderboard in stats (streak.py)
- Per-tag deterministic colors
- Batch delete multiple tasks
- Weekly report command
- Color themes: default / pastel / mono

## Modules
| File             | Purpose                            |
|------------------|------------------------------------|
| todo.py          | Main app and CLI loop              |
| tui.py           | Interactive terminal UI            |
| focus.py         | Pomodoro focus timer               |
| hooks.py         | Event system for hooks             |
| notification.py  | Desktop notifications              |
| template.py      | Task templates                     |
| streak.py        | Streak analytics                   |
| search.py        | Ranked search engine               |
| validator.py     | Input validation                   |
| cli.py           | Prompt and display helpers         |
| colors.py        | ANSI colors and themes             |
| recur.py         | Recurring task scheduling          |
| notes.py         | Per-task notes                     |
| report.py        | Daily and weekly reports           |
| progressbar.py   | Unicode progress bar               |
| csvio.py         | CSV import and export              |
| db.py            | SQLite persistence                 |
| migrate.py       | JSON to SQLite migration           |
| config.py        | App-wide configuration             |

## Run

python todo.py

