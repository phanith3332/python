# task4_repeat_decorator.py

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
@repeat(3)
def greet(name):
    print("Hello,", name)
# Call the decorated function
greet("Phanith")

'''output:
Hello, Phanith
Hello, Phanith
Hello, Phanith'''
