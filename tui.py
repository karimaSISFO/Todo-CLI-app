import os
import sys

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def terminal_size():
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines
    except OSError:
        return 80, 24

def draw_box(title, width=60):
    print("┌" + "─" * (width - 2) + "┐")
    pad = (width - 2 - len(title)) // 2
    print("│" + " " * pad + title + " " * (width - 2 - pad - len(title)) + "│")
    print("├" + "─" * (width - 2) + "┤")

def draw_footer(text, width=60):
    print("├" + "─" * (width - 2) + "┤")
    pad = width - 2 - len(text)
    print("│ " + text + " " * (pad - 1) + "│")
    print("└" + "─" * (width - 2) + "┘")

def draw_row(text, width=60, selected=False):
    prefix = "▶ " if selected else "  "
    content = prefix + text
    if len(content) > width - 4:
        content = content[:width - 7] + "..."
    pad = width - 2 - len(content)
    print("│" + content + " " * pad + "│")

def render_task_row(i, task, selected=False, width=60):
    pri_sym = {"HIGH": "!", "MED": "-", "LOW": "·"}.get(task["priority"], "-")
    check   = "x" if task["done"] else " "
    pin     = "📌" if task.get("pinned") else "  "
    streak  = f"🔥{task['streak']}" if task.get("streak") else ""
    due     = f" [{task['due']}]" if task.get("due") else ""
    title   = task["title"]
    text    = f"[{check}] {pri_sym} {pin} {title}{due} {streak}"
    draw_row(text, width, selected)

def render_task_list(todos, selected_idx=0, width=60):
    draw_box("TODO LIST", width)
    if not todos:
        draw_row("No tasks. Press 'a' to add.", width)
    for i, task in enumerate(todos):
        render_task_row(i + 1, task, selected=(i == selected_idx), width=width)
    draw_footer(f"{len(todos)} tasks | a:add d:done x:del q:quit", width)
