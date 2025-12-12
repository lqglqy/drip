import re


def scan(payload: dict):
    # payload is expected to contain 'path' or 'text' for demo purposes
    text = payload.get("text") or ""
    patterns = payload.get("patterns", [r"secret", r"password"])
    matches = []
    for p in patterns:
        matches.extend(re.findall(p, text, flags=re.IGNORECASE))
    return matches
