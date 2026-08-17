_hooks = {}

def register(event, fn):
    _hooks.setdefault(event, []).append(fn)

def fire(event, payload=None):
    for fn in _hooks.get(event, []):
        try:
            fn(payload)
        except Exception as e:
            print(f"[hook error] {event}: {e}")

def clear_hooks(event=None):
    if event:
        _hooks.pop(event, None)
    else:
        _hooks.clear()
