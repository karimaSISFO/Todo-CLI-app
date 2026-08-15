import json
import os
from db import init_db, insert_task

def migrate_from_json(json_file="todos.json"):
    if not os.path.exists(json_file):
        print(f"No {json_file} found, nothing to migrate.")
        return
    init_db()
    with open(json_file) as f:
        tasks = json.load(f)
    for task in tasks:
        task.setdefault("repeat", None)
        task.setdefault("streak", 0)
        task.setdefault("notes",  [])
        insert_task(task)
    print(f"Migrated {len(tasks)} tasks from {json_file} to todos.db")

if __name__ == "__main__":
    migrate_from_json()
