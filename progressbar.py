def bar(done, total, width=20):
    if total == 0:
        return "[" + "-" * width + "] 0%"
    pct   = min(done / total, 1.0)
    filled = int(width * pct)
    return f"[{'█' * filled}{'░' * (width - filled)}] {int(pct*100)}%"
