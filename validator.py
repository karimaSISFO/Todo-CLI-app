from datetime import datetime

PRIORITIES = ["HIGH", "MED", "LOW"]
REPEATS    = ["daily", "weekly", "monthly", None]

def validate_title(title):
    if not title or not title.strip():
        return False, "Title cannot be empty."
    title = title.strip()
    if len(title) > 200:
        return False, "Title too long (max 200 chars)."
    return True, None

def validate_priority(priority):
    if priority not in PRIORITIES:
        return False, f"Priority must be one of: {', '.join(PRIORITIES)}"
    return True, None

def validate_due(due):
    if not due:
        return True, None
    try:
        datetime.strptime(due, "%Y-%m-%d")
        return True, None
    except ValueError:
        return False, "Due date must be YYYY-MM-DD format."

def validate_repeat(repeat):
    if repeat not in REPEATS:
        return False, f"Repeat must be: daily, weekly, monthly, or empty."
    return True, None
