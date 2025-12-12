import os


def scan(payload: dict):
    # Example: return basic metadata for a path
    path = payload.get("path")
    if not path:
        return {}
    try:
        stat = os.stat(path)
        return {"size": stat.st_size, "mtime": stat.st_mtime}
    except Exception:
        return {}
