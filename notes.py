import os
import json

NOTES_FILE = "notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return {}
    with open(NOTES_FILE) as f:
        return json.load(f)

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(task_id, text):
    notes = load_notes()
    key = str(task_id)
    if key not in notes:
        notes[key] = []
    notes[key].append({"text": text, "at": __import__("datetime").datetime.now().isoformat()})
    save_notes(notes)
    print(f"Note added to task {task_id}.")

def get_notes(task_id):
    notes = load_notes()
    return notes.get(str(task_id), [])

def delete_notes(task_id):
    notes = load_notes()
    notes.pop(str(task_id), None)
    save_notes(notes)
