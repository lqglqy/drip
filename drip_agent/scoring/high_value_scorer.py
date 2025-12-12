def score(features: dict) -> int:
    # Very small MVP scoring: sum some numeric features
    s = 0
    for k, v in features.items():
        if isinstance(v, (int, float)):
            s += int(v)
    return max(0, min(100, s))
