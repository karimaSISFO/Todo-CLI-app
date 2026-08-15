def score_task(task, keyword):
    kw = keyword.lower()
    score = 0
    if kw in task["title"].lower():
        score += 10
        if task["title"].lower().startswith(kw):
            score += 5
    for tag in task.get("tags", []):
        if kw in tag.lower():
            score += 3
    if task.get("due") and kw in task["due"]:
        score += 2
    for note in task.get("notes", []):
        if kw in note.get("text","").lower():
            score += 1
    if not task["done"]:
        score += 1
    return score

def ranked_search(todos, keyword):
    results = [(score_task(t, keyword), t) for t in todos]
    results = [(s, t) for s, t in results if s > 0]
    results.sort(key=lambda x: x[0], reverse=True)
    return [t for _, t in results]
