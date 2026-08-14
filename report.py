from datetime import datetime

def daily_report(todos):
    today     = datetime.now().strftime("%Y-%m-%d")
    done      = [t for t in todos if t["done"]]
    pending   = [t for t in todos if not t["done"]]
    due_today = [t for t in todos if t.get("due") == today and not t["done"]]
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
