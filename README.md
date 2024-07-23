# session-6-assignment-shanerodricks

# Session 6: Advanced Closures in Python

# Project Description
This project involves writing and testing various closures in Python. Each closure has a specific functionality, and the overall project is designed to enhance understanding and application of closures. The project includes creating closures for checking docstring lengths, generating Fibonacci numbers, counting function calls, and updating different dictionaries with function call counts.

# Functionality

# Closure to Check Docstring Length
A closure that takes a function and checks whether the function has a docstring with more than 50 characters. The number 50 is stored as a free variable.

# Function Defintion: 
def docstring_length_checker():
    min_length = 50
    
    def checker(func):
        if func.__doc__ and len(func.__doc__) > min_length:
            return True
        else:
            return False
    
    return checker

- Test Cases: 4

# Closure for Fibonacci Sequence
The Fibonacci sequence is a series of numbers where each number (after the first two) is the sum of the two preceding ones. The sequence typically starts with 0 and 1. For example, the beginning of the sequence is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on. This sequence appears in various aspects of mathematics and nature, such as the branching of trees, the arrangement of leaves on a stem, and the flowering of artichokes.

# Function Definition:
def fibonacci_generator():
    a, b = 0, 1
    
    def next_fibonacci():
        nonlocal a, b
        fib = a
        a, b = b, a + b
        return fib
    
    return next_fibonacci

- Test Cases: 2

# Closure to Count Function Calls
A closure that counts how many times the add, mul, and div functions are called. The counts are updated in a global dictionary variable.

# Function Definition:
global_call_counts = {'add': 0, 'mul': 0, 'div': 0}

def function_call_counter():
    def counter(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            global_call_counts[func.__name__] += 1
            return result
        return wrapper
    return counter

- Test Cases: 6

# Closure to Use Different Dictionaries
Modification of the above closure to accept different dictionary variables, allowing updates to different dictionaries with function call counts.

# Function Definition:
def function_call_counter(dict_var):
    def counter(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            dict_var[func.__name__] += 1
            return result
        return wrapper
    return counter

- Test Cases: 6

# Testing
The project requires at least 25 test cases, with a minimum of 7 test cases to check boundary conditions that might cause the code to fail. The test cases will cover:
- Checking the docstring length of various functions.
- Generating Fibonacci numbers and validating the sequence.
- Counting function calls for add, mul, and div functions.
- Updating different dictionaries with function call counts.

# Example Test Cases:
import unittest

from closure_module import (
    docstring_length_checker, fibonacci_generator, function_call_counter
)

class TestClosures(unittest.TestCase):

    def test_docstring_length_checker(self):
        checker = docstring_length_checker()
        
        def test_func():
            """This function has a docstring with more than fifty characters for testing purposes."""
            pass

        def short_docstring_func():
            """Short docstring."""
            pass
        
        self.assertTrue(checker(test_func))
        self.assertFalse(checker(short_docstring_func))

    def test_fibonacci_generator(self):
        fib_gen = fibonacci_generator()
        self.assertEqual(fib_gen(), 0)
        self.assertEqual(fib_gen(), 1)
        self.assertEqual(fib_gen(), 1)
        self.assertEqual(fib_gen(), 2)
        self.assertEqual(fib_gen(), 3)
        self.assertEqual(fib_gen(), 5)
        
    def test_function_call_counter_global(self):
        global_call_counts = {'add': 0, 'mul': 0, 'div': 0}
        
        @function_call_counter()
        def add(a, b):
            return a + b
        
        @function_call_counter()
        def mul(a, b):
            return a * b
        
        @function_call_counter()
        def div(a, b):
            return a / b
        
        add(1, 2)
        add(3, 4)
        mul(2, 3)
        div(10, 2)
        
        self.assertEqual(global_call_counts['add'], 2)
        self.assertEqual(global_call_counts['mul'], 1)
        self.assertEqual(global_call_counts['div'], 1)

    def test_function_call_counter_different_dict(self):
        local_call_counts = {'add': 0, 'mul': 0, 'div': 0}
        
        @function_call_counter(local_call_counts)
        def add(a, b):
            return a + b
        
        @function_call_counter(local_call_counts)
        def mul(a, b):
            return a * b
        
        @function_call_counter(local_call_counts)
        def div(a, b):
            return a / b
        
        add(1, 2)
        add(3, 4)
        mul(2, 3)
        div(10, 2)
        
        self.assertEqual(local_call_counts['add'], 2)
        self.assertEqual(local_call_counts['mul'], 1)
        self.assertEqual(local_call_counts['div'], 1)

# Deployment
1. Upload the Code to GitHub: Ensure the code is uploaded to a GitHub repository.
2. Run GitHub Actions: Set up GitHub Actions for automated testing.
3. Proceed to answer the assignment solutions after running the tests.