import os

todos = []
done = []
SAVE_FILE = "todos.txt"

def add_todo(task):
    if not task:
        print("Task cannot be empty.")
        return
    todos.append(task)
    print(f"Added: {task}")

def list_todos():
    if not todos:
        print("No todos yet.")
        return
    for i, todo in enumerate(todos, 1):
        status = "[x]" if todo in done else "[ ]"
        print(f"{i}. {status} {todo}")

def delete_todo(index):
    if index < 1 or index > len(todos):
        print("Invalid index.")
        return
    removed = todos.pop(index - 1)
    print(f"Deleted: {removed}")

def complete_todo(index):
    if index < 1 or index > len(todos):
        print("Invalid index.")
        return
    task = todos[index - 1]
    done.append(task)
    print(f"Completed: {task}")

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

if __name__ == "__main__":
    load_todos()
    while True:
        cmd = input("Command (add/list/done/del/save/quit): ").strip()
        if cmd == "quit":
            break
        elif cmd == "add":
            task = input("Task: ").strip()
            add_todo(task)
        elif cmd == "list":
            list_todos()
        elif cmd == "done":
            try:
                idx = int(input("Task number: "))
                complete_todo(idx)
            except ValueError:
                print("Please enter a valid number.")
        elif cmd == "del":
            try:
                idx = int(input("Task number: "))
                delete_todo(idx)
            except ValueError:
                print("Please enter a valid number.")
        elif cmd == "save":
            save_todos()
        else:
            print("Unknown command.")
# WIP: priority support — format not decided yet
# todos will store as "HIGH|Buy groceries"
