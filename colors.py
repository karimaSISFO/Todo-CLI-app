RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RED    = "\033[31m"
YELLOW = "\033[93m"
GREEN  = "\033[32m"
CYAN   = "\033[36m"
GRAY   = "\033[90m"
BLUE   = "\033[34m"
MAGENTA= "\033[35m"

PRIORITY_COLOR = {
    "HIGH": "\033[31m",
    "MED":  "\033[93m",
    "LOW":  "\033[90m",
}

def colorize(text, color):
    return f"{color}{text}{RESET}"

def bold(text):
    return f"{BOLD}{text}{RESET}"

def dim(text):
    return f"{DIM}{text}{RESET}"

THEMES = {
    "default": {
        "accent":  "\033[36m",
        "success": "\033[32m",
        "warning": "\033[93m",
        "error":   "\033[31m",
    },
    "pastel": {
        "accent":  "\033[96m",
        "success": "\033[92m",
        "warning": "\033[33m",
        "error":   "\033[91m",
    },
    "mono": {
        "accent":  "\033[1m",
        "success": "\033[1m",
        "warning": "\033[2m",
        "error":   "\033[7m",
    },
}

_active_theme = "default"

def set_theme(name):
    global _active_theme
    if name in THEMES:
        _active_theme = name

def theme_color(role):
    return THEMES.get(_active_theme, THEMES["default"]).get(role, RESET)
