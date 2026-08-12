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
        print(f"{i}. {todo}")

def delete_todo(index):
    removed = todos.pop(index - 1)
    print(f"Deleted: {removed}")

def complete_todo(index):
    task = todos[index]  # bug: off-by-one again
    done.append(task)
    todos.remove(task)
    print(f"Completed: {task}")
