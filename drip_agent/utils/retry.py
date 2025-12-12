import time
from functools import wraps


def retry(times=3, delay=1):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            last = None
            for _ in range(times):
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    last = e
                    time.sleep(delay)
            raise last

        return wrapped

    return decorator
