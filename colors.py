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
