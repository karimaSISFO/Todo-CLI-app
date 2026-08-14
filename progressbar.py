def bar(done, total, width=20):
    if total == 0:
        return "[" + "-" * width + "] 0%"
    pct   = done / total
    filled = int(width * pct)
    return f"[{'█' * filled}{'░' * (width - filled)}] {int(pct*100)}%"
