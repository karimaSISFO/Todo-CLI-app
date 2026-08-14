    import os
import json
from datetime import datetime

SAVE_FILE = "todos.json"
PRIORITIES = ["HIGH", "MED", "LOW"]
todos = []
history = []

def make_task(title, priority="MED", due=None, tags=None, repeat=None):
    return {
        "id":      int(datetime.now().timestamp() * 1000),
        "title":   title,
        "priority": priority if priority in PRIORITIES else "MED",
        "done":    False,
        "created": datetime.now().isoformat(),
        "due":     due,
        "tags":    tags or [],
        "repeat":  repeat if repeat in ("daily","weekly","monthly") else None,
        "streak":  0,
    }

RESET  = "\033[0m"
BOLD   = "\033[1m"
RED    = "\033[31m"
YELLOW = "\033[93m"
GREEN  = "\033[32m"
CYAN   = "\033[36m"
GRAY   = "\033[90m"
PRIORITY_COLOR = {"HIGH": "\033[31m", "MED": "\033[93m", "LOW": "\033[90m"}

def colorize(text, color):
    return f"{color}{text}{RESET}"

def print_task(i, task):
    pri   = task["priority"]
    color = PRIORITY_COLOR.get(pri, RESET)
    check = colorize("[x]", GREEN) if task["done"] else colorize("[ ]", GRAY)
    title = colorize(task["title"], BOLD)
    label = colorize(f"[{pri}]", color)
    due   = colorize(f" due:{task['due']}", RED) if task["due"] else ""
    tags  = (" " + " ".join(colorize(f"#{t}", CYAN) for t in task["tags"])) if task["tags"] else ""
    print(f"  {i}. {check} {label} {title}{due}{tags}")

def parse_tags(raw):
    return [t.lstrip("#").strip() for t in raw.split() if t.strip()]

def add_todo(title, priority="MED", due=None, tags=None):
    if not title:
        print(colorize("Error: title cannot be empty.", RED))
        return
    task = make_task(title, priority, due, tags)
    todos.append(task)
    history.append(("add", task["id"]))
    print(colorize(f"Added: {title}", GREEN))

def list_todos(show_done=True):
    visible = todos if show_done else [t for t in todos if not t["done"]]
    if not visible:
        print(colorize("  No tasks found.", GRAY))
        return
    print(colorize(f"\n  Tasks ({len(visible)}):", BOLD))
    for i, task in enumerate(visible, 1):
        print_task(i, task)
    print()

def complete_todo(index):
    if index < 1 or index > len(todos):
        print(colorize("Invalid task number.", RED))
        return
    task = todos[index - 1]
    task["done"] = True
    history.append(("complete", task["id"]))
    print(colorize(f"Completed: {task['title']}", GREEN))

def delete_todo(index):
    if index < 1 or index > len(todos):
        print(colorize("Invalid task number.", RED))
        return
    task = todos.pop(index - 1)
    history.append(("delete", task))
    print(colorize(f"Deleted: {task['title']}", YELLOW))

def undo():
    if not history:
        print(colorize("Nothing to undo.", GRAY))
        return
    action, payload = history.pop()
    if action == "add":
        todos[:] = [t for t in todos if t["id"] != payload]
        print(colorize("Undid last add.", YELLOW))
    elif action == "complete":
        for t in todos:
            if t["id"] == payload:
                t["done"] = False
                print(colorize(f"Undid complete: {t['title']}", YELLOW))
                break
    elif action == "delete":
        todos.append(payload)
        todos.sort(key=lambda t: t["created"])
        print(colorize(f"Restored: {payload['title']}", GREEN))
    else:
        print(colorize(f"Cannot undo: {action}", RED))

def save_todos():
    with open(SAVE_FILE, "w") as f:
        json.dump(todos, f, indent=2)
    print(colorize(f"Saved {len(todos)} tasks to {SAVE_FILE}", GREEN))

def load_todos():
    if not os.path.exists(SAVE_FILE):
        return
    try:
        with open(SAVE_FILE) as f:
            data = json.load(f)
        todos.extend(data)
        print(colorize(f"Loaded {len(data)} tasks.", CYAN))
    except (json.JSONDecodeError, KeyError):
        print(colorize("Warning: save file corrupted, starting fresh.", YELLOW))

def export_json(path="export.json"):
    with open(path, "w") as f:
        json.dump({
            "exported": datetime.now().isoformat(),
            "total":    len(todos),
            "tasks":    todos,
        }, f, indent=2)
    print(colorize(f"Exported to {path}", GREEN))

def filter_by_tag(tag):
    tag = tag.lstrip("#").lower()
    results = [t for t in todos if tag in [x.lower() for x in t["tags"]]]
    if not results:
        print(colorize(f"No tasks with tag #{tag}", GRAY))
        return
    print(colorize(f"\n  Tagged #{tag}:", BOLD))
    for i, task in enumerate(results, 1):
        print_task(i, task)
    print()

def filter_by_priority(pri):
    pri = pri.upper()
    results = [t for t in todos if t["priority"] == pri]
    if not results:
        print(colorize(f"No {pri} tasks.", GRAY))
        return
    print(colorize(f"\n  {pri} tasks:", BOLD))
    for i, task in enumerate(results, 1):
        print_task(i, task)
    print()

def get_overdue():
    today = datetime.now().date()
    result = []
    for t in todos:
        if t["due"] and not t["done"]:
            try:
                if datetime.fromisoformat(t["due"]).date() < today:
                    result.append(t)
            except ValueError:
                pass
    return result

def stats():
    total   = len(todos)
    done_ct = sum(1 for t in todos if t["done"])
    overdue = len(get_overdue())
    by_pri  = {p: sum(1 for t in todos if t["priority"] == p) for p in PRIORITIES}
    print(colorize("\n  ── Stats ───────────────────────", BOLD))
    print(f"  Total   : {total}")
    print(f"  Done    : {colorize(str(done_ct), GREEN)}")
    print(f"  Pending : {colorize(str(total - done_ct), YELLOW)}")
    print(f"  Overdue : {colorize(str(overdue), RED)}")
    for p in PRIORITIES:
        print(f"  {colorize(p, PRIORITY_COLOR[p]):<22}: {by_pri[p]}")
    print()

def search(keyword):
    kw = keyword.lower()
    def matches(t):
        return kw in t["title"].lower() or any(kw in tag.lower() for tag in t["tags"])
    results = [t for t in todos if matches(t)]
    if not results:
        print(colorize(f"No results for '{keyword}'", GRAY))
        return
    print(colorize(f"
  Results for '{keyword}':", BOLD))
    for i, task in enumerate(results, 1):
        print_task(i, task)
    print()

def edit_task(index, title=None, priority=None, due=None, tags=None):
    if index < 1 or index > len(todos):
        print(colorize("Invalid task number.", RED))
        return
    task = todos[index - 1]
    if title:    task["title"]    = title
    if priority and priority in PRIORITIES: task["priority"] = priority
    if due is not None: task["due"] = due or None
    if tags is not None: task["tags"] = tags
    print(colorize(f"Updated: {task['title']}", GREEN))

def sort_todos(by="priority"):
    pri_order = {"HIGH": 0, "MED": 1, "LOW": 2}
    if by == "priority":
        todos.sort(key=lambda t: pri_order.get(t["priority"], 9))
    elif by == "due":
        def due_key(t):
            if not t["due"]:
                return datetime(9999, 12, 31)
            try:
                return datetime.fromisoformat(t["due"])
            except ValueError:
                return datetime(9999, 12, 31)
        todos.sort(key=due_key)
    elif by == "title":
        todos.sort(key=lambda t: t["title"].lower())
    print(colorize(f"Sorted by {by}.", CYAN))

def get_index(prompt="Task number: "):
    try:
        return int(input(f"  {prompt}"))
    except ValueError:
        print(colorize("Please enter a valid number.", RED))
        return None

HELP = colorize("""
  add      Add new task          list     List all tasks
  pending  Pending tasks only    done     Mark complete
  del      Delete task           edit     Edit task fields
  undo     Undo last action      search   Search by keyword
  tag      Filter by tag         pri      Filter by priority
  sort     Sort tasks            overdue  Show overdue
  stats    Statistics            save     Save to file
  export   Export JSON           quit     Save and exit
""", CYAN)

if __name__ == "__main__":
    load_todos()
    overdue = get_overdue()
    if overdue:
        print(colorize(f"\n  ⚠ {len(overdue)} overdue task(s)!", RED))
    print(colorize("\n  Todo CLI v2.0", BOLD) + colorize("  type 'help' for commands\n", GRAY))

    while True:
        try:
            cmd = input(colorize("  > ", CYAN)).strip().lower()
        except (KeyboardInterrupt, EOFError):
            print()
            save_todos()
            break

        if cmd == "quit":
            save_todos(); break
        elif cmd == "help":
            print(HELP)
        elif cmd == "add":
            title    = input("  Title: ").strip()
            pri      = input("  Priority (HIGH/MED/LOW) [MED]: ").strip().upper() or "MED"
            due      = input("  Due date YYYY-MM-DD (optional): ").strip() or None
            raw_tags = input("  Tags e.g. work personal (optional): ").strip()
            add_todo(title, pri, due, parse_tags(raw_tags) if raw_tags else [])
        elif cmd == "list":
            list_todos()
        elif cmd == "pending":
            list_todos(show_done=False)
        elif cmd == "done":
            list_todos()
            idx = get_index()
            if idx: complete_todo(idx)
        elif cmd == "del":
            list_todos()
            idx = get_index()
            if idx: delete_todo(idx)
        elif cmd == "edit":
            list_todos()
            idx = get_index()
            if idx:
                title    = input("  New title (enter to skip): ").strip() or None
                pri      = input("  New priority (enter to skip): ").strip().upper() or None
                due      = input("  New due date (enter to skip, 'clear' to remove): ").strip()
                raw_tags = input("  New tags (enter to skip): ").strip()
                edit_task(idx, title, pri,
                          "" if due == "clear" else due or None,
                          parse_tags(raw_tags) if raw_tags else None)
        elif cmd == "undo":
            undo()
        elif cmd == "search":
            kw = input("  Keyword: ").strip()
            search(kw)
        elif cmd == "tag":
            tag = input("  Tag: ").strip()
            filter_by_tag(tag)
        elif cmd == "pri":
            pri = input("  Priority (HIGH/MED/LOW): ").strip()
            filter_by_priority(pri)
        elif cmd == "sort":
            by = input("  Sort by (priority/due/title) [priority]: ").strip() or "priority"
            sort_todos(by)
        elif cmd == "overdue":
            results = get_overdue()
            if not results:
                print(colorize("  No overdue tasks.", GREEN))
            else:
                print(colorize(f"\n  Overdue ({len(results)}):", RED))
                for i, task in enumerate(results, 1):
                    print_task(i, task)
                print()
        elif cmd == "stats":
            stats()
        elif cmd == "save":
            save_todos()
        elif cmd == "export":
            path = input("  Output file [export.json]: ").strip() or "export.json"
            export_json(path)
        else:
            print(colorize(f"  Unknown command: '{cmd}'. Type 'help'.", GRAY))
