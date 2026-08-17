import subprocess
import platform

def notify(title, message):
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "{title}"'
            ], check=False)
        elif system == "Linux":
            subprocess.run(["notify-send", title, message], check=False)
        elif system == "Windows":
            # requires win10toast or plyer in prod
            print(f"[notify] {title}: {message}")
    except Exception:
        pass  # silently skip if notify unavailable
