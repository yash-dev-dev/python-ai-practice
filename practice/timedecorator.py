from functools import wraps
import time
def timer(func):
    @wraps(func)
    def wrapper(*args,**keyargs):
        start=time.time()
        result=func(*args,**keyargs)
        end=time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        
        return result
    return wrapper


@timer
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total
slow_function()