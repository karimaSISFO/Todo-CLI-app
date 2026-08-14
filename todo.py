
def show_notes(index):
    if index < 1 or index > len(todos):
        print(colorize("Invalid task number.", RED))
        return
    task  = todos[index - 1]
    items = get_notes(task["id"])
    if not items:
        print(colorize(f"  No notes for: {task['title']}", GRAY))
        return
    print(colorize(f"\n  Notes for: {task['title']}", BOLD))
    for i, n in enumerate(items, 1):
        print(f"  {i}. {n['text']}", colorize(f"  ({n['at'][:10]})", GRAY))
    print()

def bulk_complete(indices):
    for idx in indices:
        if idx < 1 or idx > len(todos):
            print(colorize(f"  Skipping invalid index: {idx}", GRAY))
            continue
        task = todos[idx - 1]
        if task["done"]:
            print(colorize(f"  Already done: {task['title']}", GRAY))
            continue
        task["done"] = True
        history.append(("complete", task["id"]))
        print(colorize(f"  Completed: {task['title']}", GREEN))
