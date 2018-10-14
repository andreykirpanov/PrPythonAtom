def cache_decorator(func):
    cache = {}
    def cached(n: int):
        if n in cache:
            return cache[n]
        else:
            res = func(n)
            cache[n] = res
            return res
    return cached
	
@cache_decorator
def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 2 else 1