todos = []
done = []

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

if __name__ == "__main__":
    while True:
        cmd = input("Command (add/list/done/del/quit): ").strip()
        if cmd == "quit":
            break
        elif cmd == "add":
            task = input("Task: ").strip()
            add_todo(task)
        elif cmd == "list":
            list_todos()
        elif cmd == "done":
            idx = int(input("Task number: "))
            complete_todo(idx)
        elif cmd == "del":
            idx = int(input("Task number: "))
            delete_todo(idx)
        else:
            print("Unknown command.")
