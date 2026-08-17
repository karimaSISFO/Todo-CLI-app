from datetime import datetime, timedelta

def longest_streak(todos):
    """Find task with highest streak count."""
    candidates = [t for t in todos if t.get("streak", 0) > 0]
    if not candidates:
        return None, 0
    best = max(candidates, key=lambda t: t["streak"])
    return best["title"], best["streak"]

def streak_summary(todos):
    active = [(t["title"], t["streak"]) for t in todos if t.get("streak", 0) > 0]
    active.sort(key=lambda x: x[1], reverse=True)
    return active

def total_completions(todos):
    return sum(t.get("streak", 0) for t in todos)
