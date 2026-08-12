todos = []

def add_todo(task):
    todos.append(task)
    print(f"Added: {task}")

def list_todos():
    for todo in todos:
        print(f"- {todo}")
