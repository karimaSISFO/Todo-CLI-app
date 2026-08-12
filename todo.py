todos = []
done = []

def add_todo(task):
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
    removed = todos.pop(index - 1)
    print(f"Deleted: {removed}")

def complete_todo(index):
    task = todos[index - 1]
    done.append(task)
    print(f"Completed: {task}")
