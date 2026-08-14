
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

def archive_done():
    done_tasks = [t for t in todos if t["done"]]
    if not done_tasks:
        print(colorize("No completed tasks to archive.", GRAY))
        return
    archive_file = "archive.json"
    existing = []
    if os.path.exists(archive_file):
        with open(archive_file) as f:
            existing = json.load(f)
    existing.extend(done_tasks)
    with open(archive_file, "w") as f:
        json.dump(existing, f, indent=2)
    todos[:] = [t for t in todos if not t["done"]]
    print(colorize(f"Archived {len(done_tasks)} completed task(s).", GREEN))
