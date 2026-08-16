import json
import os

TEMPLATE_FILE = "templates.json"

def load_templates():
    if not os.path.exists(TEMPLATE_FILE):
        return {}
    with open(TEMPLATE_FILE) as f:
        return json.load(f)

def save_templates(templates):
    with open(TEMPLATE_FILE, "w") as f:
        json.dump(templates, f, indent=2)

def add_template(name, task):
    templates = load_templates()
    templates[name] = {
        "priority": task.get("priority", "MED"),
        "tags":     task.get("tags", []),
        "repeat":   task.get("repeat"),
        "due":      None,
    }
    save_templates(templates)
    return name

def get_template(name):
    return load_templates().get(name)

def list_templates():
    return list(load_templates().keys())
