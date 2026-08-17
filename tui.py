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
