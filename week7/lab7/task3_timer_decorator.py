# task3_timer_decorator.py

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.6f} seconds")
        return result
    return wrapper
@timer
def calculate_sum():
    total = 0
    for i in range(1, 10_000_001):
        total += i
    return total
result = calculate_sum()
print("Sum:", result)

'''output:
calculate_sum took 0.363944 seconds
Sum: 50000005000000'''

