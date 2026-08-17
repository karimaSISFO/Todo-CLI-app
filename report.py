from datetime import datetime

def daily_report(todos):
    today     = datetime.now().strftime("%Y-%m-%d")
    done      = [t for t in todos if t["done"]]
    pending   = [t for t in todos if not t["done"]]
    due_today = [t for t in todos if t.get("due","").startswith(today) and not t["done"]]
    lines = [
        f"=== Daily Report — {today} ===",
        f"Total tasks : {len(todos)}",
        f"Completed   : {len(done)}",
        f"Pending     : {len(pending)}",
        f"Due today   : {len(due_today)}",
    ]
    if due_today:
        lines.append("\nDue today:")
        for t in due_today:
            lines.append(f"  - [{t['priority']}] {t['title']}")
    return "\n".join(lines)

def save_report(todos, path="report.txt"):
    content = daily_report(todos)
    with open(path, "w") as f:
        f.write(content)
    return path

def _safe_date(s):
    try:
        from datetime import datetime
        return datetime.fromisoformat(s).date()
    except (ValueError, TypeError):
        return None

def _safe_date(s):
    try:
        from datetime import datetime
        return datetime.fromisoformat(s).date()
    except (ValueError, TypeError):
        return None

def weekly_report(todos):
    from datetime import datetime, timedelta
    today  = datetime.now().date()
    start  = today - timedelta(days=today.weekday())
    end    = start + timedelta(days=6)
    done   = [t for t in todos if t["done"]]
    week_done = [
        t for t in done
        if t.get("created") and _safe_date(t["created"]) and
        start <= _safe_date(t["created"]) <= end
    ]
    lines = [
        f"=== Weekly Report — {start} to {end} ===",
        f"Completed this week : {len(week_done)}",
        f"Total tasks         : {len(todos)}",
        f"Still pending       : {sum(1 for t in todos if not t['done'])}",
    ]
    if week_done:
        lines.append("\nCompleted this week:")
        for t in week_done:
            lines.append(f"  ✓ {t['title']}")
    return "\n".join(lines)

def _safe_date(s):
    try:
        from datetime import datetime
        return datetime.fromisoformat(s).date()
    except (ValueError, TypeError):
        return None

def weekly_report(todos):
    from datetime import datetime, timedelta
    today  = datetime.now().date()
    start  = today - timedelta(days=today.weekday())
    end    = start + timedelta(days=6)
    done   = [t for t in todos if t["done"]]
    week_done = [
        t for t in done
        if t.get("created") and _safe_date(t["created"]) and
        start <= _safe_date(t["created"]) <= end
    ]
    lines = [
        f"=== Weekly Report — {start} to {end} ===",
        f"Completed this week : {len(week_done)}",
        f"Total tasks         : {len(todos)}",
        f"Still pending       : {sum(1 for t in todos if not t['done'])}",
    ]
    if week_done:
        lines.append("\nCompleted this week:")
        for t in week_done:
            lines.append(f"  ✓ {t['title']}")
    return "\n".join(lines)
