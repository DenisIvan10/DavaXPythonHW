from app.cache import cache  

def pow_op(base: int, exp: int) -> int:
    key = f"pow:{base}:{exp}"
    result = cache.get(key)
    if result is not None:
        return result
    result = base ** exp
    cache.set(key, result)
    return result

def factorial_op(n: int) -> int:
    key = f"factorial:{n}"
    result = cache.get(key)
    if result is not None:
        return result
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    cache.set(key, result)
    return result

def fibonacci_op(n: int) -> int:
    key = f"fibonacci:{n}"
    result = cache.get(key)
    if result is not None:
        return result
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    cache.set(key, a)
    return a
