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
