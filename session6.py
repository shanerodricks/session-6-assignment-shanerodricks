# Closure to Check Docstring Length
def docstring_length_checker():
    min_length = 50
    
    def checker(func):
        if func.__doc__ and len(func.__doc__) > min_length:
            return True
        else:
            return False
    
    return checker


# Closure for Fibonacci Sequence
def fibonacci_generator():
    a, b = 0, 1
    
    def next_fibonacci():
        nonlocal a, b
        fib = a
        a, b = b, a + b
        return fib
    
    return next_fibonacci


# Closure to Count Function Calls
global_call_counts = {'add': 0, 'mul': 0, 'div': 0}

def function_call_counter():
    def counter(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            global_call_counts[func.__name__] += 1
            return result
        return wrapper
    return counter


# Closure to Use Different Dictionaries
def function_call_counter(dict_var):
    def counter(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            dict_var[func.__name__] += 1
            return result
        return wrapper
    return counter
