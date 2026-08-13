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
