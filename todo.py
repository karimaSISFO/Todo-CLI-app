import os

todos = []
done = []
SAVE_FILE = "todos.txt"
PRIORITIES = ["HIGH", "MED", "LOW"]

def get_index(prompt="Task number: "):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None

def add_todo(task, priority="MED"):
    if not task:
        print("Task cannot be empty.")
        return
    if priority not in PRIORITIES:
        priority = "MED"
    todos.append(f"{priority}|{task}")
    print(f"[{priority}] Added: {task}")

def list_todos():
    if not todos:
        print("No todos yet.")
        return
    for i, entry in enumerate(todos, 1):
        priority, task = entry.split("|", 1)
        status = "[x]" if entry in done else "[ ]"
        print(f"{i}. {status} [{priority}] {task}")

def delete_todo(index):
    if index < 1 or index > len(todos):
        print("Invalid index.")
        return
    removed = todos.pop(index - 1)
    print(f"Deleted: {removed.split('|',1)[1]}")

def complete_todo(index):
    if index < 1 or index > len(todos):
        print("Invalid index.")
        return
    entry = todos[index - 1]
    done.append(entry)
    print(f"Completed: {entry.split('|',1)[1]}")

def save_todos():
    with open(SAVE_FILE, "w") as f:
        for t in todos:
            f.write(t + "\n")
    print(f"Saved {len(todos)} tasks.")

def load_todos():
    if not os.path.exists(SAVE_FILE):
        return
    with open(SAVE_FILE, "r") as f:
        for line in f:
            task = line.strip()
            if task:
                todos.append(task)
    print(f"Loaded {len(todos)} tasks.")

def sort_todos():
    order = {"HIGH": 0, "MED": 1, "LOW": 2}
    todos.sort(key=lambda x: order.get(x.split("|")[0], 9))
    print("Sorted by priority.")

def search_todos(keyword):
    results = [t for t in todos if keyword.lower() in t.lower()]
    for r in results:
        print(r)

def summary():
    total = len(todos)
    completed = len(done)
    pending = total - completed
    print(f"Total: {total} | Done: {completed} | Pending: {pending}")

if __name__ == "__main__":
    load_todos()
    while True:
        cmd = input("Command (add/list/done/del/save/sort/search/summary/quit): ").strip()
        if cmd == "quit":
            break
        elif cmd == "add":
            task = input("Task: ").strip()
            pri = input("Priority (HIGH/MED/LOW) [MED]: ").strip().upper() or "MED"
            add_todo(task, pri)
        elif cmd == "list":
            list_todos()
        elif cmd == "done":
            idx = get_index()
            if idx: complete_todo(idx)
        elif cmd == "del":
            idx = get_index()
            if idx: delete_todo(idx)
        elif cmd == "save":
            save_todos()
        elif cmd == "sort":
            sort_todos()
        elif cmd == "search":
            kw = input("Keyword: ").strip()
            search_todos(kw)
        elif cmd == "summary":
            summary()
        else:
            print("Unknown command.")
