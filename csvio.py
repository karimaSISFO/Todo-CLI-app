import csv
from datetime import datetime

FIELDS = ["id","title","priority","done","created","due","tags","repeat","streak"]

def export_csv(todos, path="todos.csv"):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for t in todos:
            row = dict(t)
            row["tags"] = "|".join(t.get("tags", []))
            row["done"] = int(t["done"])
            w.writerow(row)
    return path

def import_csv(path="todos.csv"):
    tasks = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["tags"]   = [x for x in row["tags"].split("|") if x]
            row["done"]   = bool(int(row.get("done", 0)))
            row["streak"] = int(row.get("streak", 0))
            row["id"]     = int(row["id"])
            tasks.append(row)
    return tasks
