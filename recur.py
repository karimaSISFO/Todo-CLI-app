from datetime import datetime, timedelta

INTERVALS = {
    "daily":   timedelta(days=1),
    "weekly":  timedelta(weeks=1),
    "monthly": None,
}

def next_due(task):
    """Return next due date string for a recurring task."""
    if not task.get("repeat") or not task.get("due"):
        return None
    repeat = task["repeat"]
    try:
        current = datetime.fromisoformat(task["due"])
    except ValueError:
        return None
    if repeat == "monthly":
        month = current.month + 1
        year  = current.year
        if month > 12:
            month = 1
            year += 1
        import calendar
        last_day = calendar.monthrange(year, month)[1]
        day = min(current.day, last_day)
        return current.replace(year=year, month=month, day=day).strftime("%Y-%m-%d")
    delta = INTERVALS[repeat]
    return (current + delta).strftime("%Y-%m-%d")
