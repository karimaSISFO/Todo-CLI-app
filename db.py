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
