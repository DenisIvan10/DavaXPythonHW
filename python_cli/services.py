from logger import logger

def calculate_pow(base: int, exp: int) -> int:
    logger.debug(f"Calculam {base} ** {exp}")
    return base ** exp

def calculate_fib(n: int) -> int:
    logger.debug(f"Calculam Fibonacci pentru n = {n}")
    if n < 0:
        raise ValueError("Fibonacci nu este definit pentru numere negative.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def calculate_fact(n: int) -> int:
    logger.debug(f"Calculam factorial pentru n = {n}")
    if n < 0:
        raise ValueError("Factorialul nu este definit pentru numere negative.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
