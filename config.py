import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG = {
    "save_file":         os.path.join(BASE_DIR, "todos.json"),
    "export_file":       os.path.join(BASE_DIR, "export.json"),
    "date_format":       "%Y-%m-%d",
    "max_undo":          20,
    "default_priority":  "MED",
}
