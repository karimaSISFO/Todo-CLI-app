import os
import json
from datetime import datetime

SAVE_FILE = "todos.json"
PRIORITIES = ["HIGH", "MED", "LOW"]
todos = []
history = []

def make_task(title, priority="MED", due=None, tags=None):
    return {
        "id":      int(datetime.now().timestamp() * 1000),
        "title":   title,
        "priority": priority if priority in PRIORITIES else "MED",
        "done":    False,
        "created": datetime.now().isoformat(),
        "due":     due,
        "tags":    tags or [],
    }

RESET  = "\033[0m"
BOLD   = "\033[1m"
RED    = "\033[31m"
YELLOW = "\033[93m"
GREEN  = "\033[32m"
CYAN   = "\033[36m"
GRAY   = "\033[90m"
PRIORITY_COLOR = {"HIGH": "\033[31m", "MED": "\033[93m", "LOW": "\033[90m"}

def colorize(text, color):
    return f"{color}{text}{RESET}"

def print_task(i, task):
    pri   = task["priority"]
    color = PRIORITY_COLOR.get(pri, RESET)
    check = colorize("[x]", GREEN) if task["done"] else colorize("[ ]", GRAY)
    title = colorize(task["title"], BOLD)
    label = colorize(f"[{pri}]", color)
    due   = colorize(f" due:{task['due']}", RED) if task["due"] else ""
    tags  = (" " + " ".join(colorize(f"#{t}", CYAN) for t in task["tags"])) if task["tags"] else ""
    print(f"  {i}. {check} {label} {title}{due}{tags}")

def parse_tags(raw):
    return [t.lstrip("#").strip() for t in raw.split() if t.strip()]

def add_todo(title, priority="MED", due=None, tags=None):
    if not title:
        print(colorize("Error: title cannot be empty.", RED))
        return
    task = make_task(title, priority, due, tags)
    todos.append(task)
    history.append(("add", task["id"]))
    print(colorize(f"Added: {title}", GREEN))

def list_todos(show_done=True):
    visible = todos if show_done else [t for t in todos if not t["done"]]
    if not visible:
        print(colorize("  No tasks found.", GRAY))
        return
    print(colorize(f"\n  Tasks ({len(visible)}):", BOLD))
    for i, task in enumerate(visible, 1):
        print_task(i, task)
    print()

def complete_todo(index):
    if index < 1 or index > len(todos):
        print(colorize("Invalid task number.", RED))
        return
    task = todos[index - 1]
    task["done"] = True
    history.append(("complete", task["id"]))
    print(colorize(f"Completed: {task['title']}", GREEN))

def delete_todo(index):
    if index < 1 or index > len(todos):
        print(colorize("Invalid task number.", RED))
        return
    task = todos.pop(index - 1)
    history.append(("delete", task))
    print(colorize(f"Deleted: {task['title']}", YELLOW))

def undo():
    if not history:
        print(colorize("Nothing to undo.", GRAY))
        return
    action, payload = history.pop()
    if action == "add":
        todos[:] = [t for t in todos if t["id"] != payload]
        print(colorize("Undid last add.", YELLOW))
    else:
        print(colorize(f"Undo not yet supported for: {action}", RED))
        history.append((action, payload))
