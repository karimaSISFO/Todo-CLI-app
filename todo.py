
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

def view_archive():
    archive_file = "archive.json"
    if not os.path.exists(archive_file):
        print(colorize("No archive found.", GRAY))
        return
    with open(archive_file) as f:
        tasks = json.load(f)
    print(colorize(f"\n  Archive ({len(tasks)} tasks):", BOLD))
    for i, task in enumerate(tasks, 1):
        print_task(i, task)
    print()

def due_soon(days=3):
    from datetime import datetime, timedelta
    today = datetime.now().date()
    cutoff = today + timedelta(days=days)
    results = [
        t for t in todos
        if t.get("due") and not t["done"]
        and today <= datetime.fromisoformat(t["due"]).date() <= cutoff
    ]
    if not results:
        print(colorize(f"  No tasks due in the next {days} day(s).", GRAY))
        return
    print(colorize(f"\n  Due in next {days} day(s):", BOLD))
    for i, task in enumerate(results, 1):
        print_task(i, task)
    print()

def pin_task(index):
    if index < 1 or index > len(todos):
        print(colorize("Invalid task number.", RED)); return
    task = todos[index - 1]
    task["pinned"] = not task.get("pinned", False)
    state = "Pinned" if task["pinned"] else "Unpinned"
    print(colorize(f"  {state}: {task['title']}", CYAN))HELP = colorize("""
  add          Add task               list         List all tasks
  pending      Pending only           done         Mark complete
  bulk         Complete many          batch-del    Delete many
  del          Delete task            edit         Edit task
  pin          Pin/unpin task         focus        Pomodoro timer
  undo         Undo last action       search       Ranked search
  tag          Filter by tag          pri          Filter priority
  sort         Sort tasks             soon         Due in N days
  overdue      Overdue tasks          stats        Stats + streaks
  note         Add/view notes         report       Daily report
  weekly       Weekly report          archive      Archive done
  archive-view Browse archive         tui          Interactive UI
  tmpl-save    Save as template       tmpl-use     Use template
  tmpl-list    List templates         theme        Color theme
  csv-export   Export CSV             csv-import   Import CSV
  save         Save to file           export       Export JSON
  quit         Save and exit
""", CYAN)_notes(index):
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

def view_archive():
    archive_file = "archive.json"
    if not os.path.exists(archive_file):
        print(colorize("No archive found.", GRAY))
        return
    with open(archive_file) as f:
        tasks = json.load(f)
    print(colorize(f"\n  Archive ({len(tasks)} tasks):", BOLD))
    for i, task in enumerate(tasks, 1):
        print_task(i, task)
    print()

def due_soon(days=3):
    from datetime import datetime, timedelta
    today = datetime.now().date()
    cutoff = today + timedelta(days=days)
    results = [
        t for t in todos
        if t.get("due") and not t["done"]
        and today <= datetime.fromisoformat(t["due"]).date() <= cutoff
    ]
    if not results:
        print(colorize(f"  No tasks due in the next {days} day(s).", GRAY))
        return
    print(colorize(f"\n  Due in next {days} day(s):", BOLD))
    for i, task in enumerate(results, 1):
        print_task(i, task)
    print()

def pin_task(index):
    if index < 1 or index > len(todos):
        print(colorize("Invalid task number.", RED)); return
    task = todos[index - 1]
    task["pinned"] = not task.get("pinned", False)
    state = "Pinned" if task["pinned"] else "Unpinned"
    print(colorize(f"  {state}: {task['title']}", CYAN))

def batch_delete(indices):
    indices = sorted({int(i) for i in indices}, reverse=True)
    deleted = 0
    for idx in indices:
        if 1 <= idx <= len(todos):
            task = todos.pop(idx - 1)
            history.append(("delete", task))
            print(colorize(f"  Deleted: {task['title']}", YELLOW))
            deleted += 1
        else:
            print(colorize(f"  Skipped invalid index: {idx}", GRAY))
    print(colorize(f"  Removed {deleted} task(s).", RED))

def batch_delete(indices):
    indices = sorted(set(indices), reverse=True)
    deleted = 0
    for idx in indices:
        if 1 <= idx <= len(todos):
            task = todos.pop(idx - 1)
            history.append(("delete", task))
            print(colorize(f"  Deleted: {task['title']}", YELLOW))
            deleted += 1
        else:
            print(colorize(f"  Skipped invalid index: {idx}", GRAY))
    print(colorize(f"  Removed {deleted} task(s).", RED))
