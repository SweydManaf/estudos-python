from functools import lru_cache

@lru_cache()
def fib(n):
    print(n)
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print(fib(100))