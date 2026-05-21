import time
from functools import wraps

def search_cache(expire_seconds: int = 300):
    cache_map = {}
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            now = time.time()
            if key in cache_map:
                res, t = cache_map[key]
                if now - t < expire_seconds:
                    return res
            result = func(*args, **kwargs)
            cache_map[key] = (result, now)
            return result
        return wrapper
    return decorator
