todos = []

def add_todo(task):
    todos.append(task)
    print(f"Added: {task}")

def list_todos():
    if not todos:
        print("No todos yet.")
        return
    for i, todo in enumerate(todos, 1):
        print(f"{i}. {todo}")
