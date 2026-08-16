import time
from datetime import datetime

def pomodoro(task_title, minutes=25):
    seconds = minutes * 60
    print(f"\n  🍅 Focus: {task_title}")
    print(f"  Duration: {minutes} min | Press Ctrl+C to stop\n")
    start = datetime.now()
    try:
        for remaining in range(seconds, 0, -1):
            m, s = divmod(remaining, 60)
            print(f"\r  ⏱  {m:02d}:{s:02d} remaining", end="", flush=True)
            time.sleep(1)
        print("\r  ✅ Focus session complete!           ")
        return True
    except KeyboardInterrupt:
        elapsed = int((datetime.now() - start).total_seconds())
        em, es  = divmod(elapsed, 60)
        print(f"\r  ⏹  Stopped after {em:02d}:{es:02d}          ")
        return False
