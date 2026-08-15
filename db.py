import sqlite3
import json
import os

DB_FILE = "todos.db"

def get_conn():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id       INTEGER PRIMARY KEY,
            title    TEXT NOT NULL,
            priority TEXT DEFAULT 'MED',
            done     INTEGER DEFAULT 0,
            created  TEXT,
            due      TEXT,
            tags     TEXT,
            repeat   TEXT,
            streak   INTEGER DEFAULT 0,
            notes    TEXT DEFAULT '[]'
        )
    """)
    conn.commit()
    conn.close()

def insert_task(task):
    conn = get_conn()
    conn.execute("""
        INSERT OR REPLACE INTO tasks
        (id, title, priority, done, created, due, tags, repeat, streak, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        task["id"],
        task["title"],
        task["priority"],
        int(task["done"]),
        task.get("created"),
        task.get("due"),
        json.dumps(task.get("tags", [])),
        task.get("repeat"),
        task.get("streak", 0),
        json.dumps(task.get("notes", [])),
    ))
    conn.commit()
    conn.close()

def fetch_all():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM tasks ORDER BY created").fetchall()
    conn.close()
    tasks = []
    for r in rows:
        tasks.append({
            "id":       r["id"],
            "title":    r["title"],
            "priority": r["priority"],
            "done":     bool(r["done"]),
            "created":  r["created"],
            "due":      r["due"],
            "tags":     json.loads(r["tags"] or "[]"),
            "repeat":   r["repeat"],
            "streak":   r["streak"],
            "notes":    json.loads(r["notes"] or "[]"),
        })
    return tasks

def delete_task(task_id):
    conn = get_conn()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def sync_all(tasks):
    """Overwrite DB with current in-memory task list."""
    conn = get_conn()
    conn.execute("DELETE FROM tasks")
    conn.commit()
    conn.close()
    for t in tasks:
        insert_task(t)
