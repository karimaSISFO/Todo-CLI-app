from colors import colorize, bold, CYAN, GRAY, RED, GREEN, YELLOW, BOLD

def prompt(text, default=None):
    suffix = f" [{default}]" if default else ""
    val = input(colorize(f"  {text}{suffix}: ", CYAN)).strip()
    return val or default

def confirm(text):
    ans = input(colorize(f"  {text} (y/n): ", YELLOW)).strip().lower()
    return ans == "y"

def section(title):
    print(colorize(f"\n  ── {title} ", BOLD) + colorize("─" * (30 - len(title)), GRAY))

def error(msg):
    print(colorize(f"  ✗ {msg}", RED))

def success(msg):
    print(colorize(f"  ✓ {msg}", GREEN))

def info(msg):
    print(colorize(f"  {msg}", CYAN))
