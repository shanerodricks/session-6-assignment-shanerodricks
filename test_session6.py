import pytest
import os
import re
import inspect
from closures import docstring_length_checker, fibonacci_generator, function_call_counter, global_call_counts

# Constants for README content checks
README_CONTENT_CHECK_FOR = [
    'docstring_length_checker',
    'fibonacci_generator',
    'function_call_counter'
]

# Test 1: README file existence
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

# Test 2: README content length
def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add at least 500 words"

# Test 3: README proper description
def test_readme_proper_description():
    READMELOOKSGOOD = True
    with open("README.md", "r") as f:
        content = f.read()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

# Test 4: README file formatting
def test_readme_file_for_formatting():
    with open("README.md", "r") as f:
        content = f.read()
    assert content.count("#") >= 10

# Test 5: Code indentation and PEP8 guidelines
def test_fourspace():
    lines = inspect.getsource(closures)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code indentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

# Test 6-9: Functionality of docstring_length_checker
def test_docstring_length_checker():
    checker = docstring_length_checker()

    def func_with_short_doc():
        """Short docstring."""
        pass

    def func_with_long_doc():
        """This is a long docstring that definitely has more than fifty characters."""
        pass

    def func_with_exactly_fifty_characters():
        """This docstring has exactly fifty characters here!"""
        pass

    def func_with_no_docstring():
        pass

    assert checker(func_with_short_doc) == False
    assert checker(func_with_long_doc) == True
    assert checker(func_with_exactly_fifty_characters) == False
    assert checker(func_with_no_docstring) == False

# Test 10-11: Functionality of fibonacci_generator
def test_fibonacci_generator():
    fib_gen = fibonacci_generator()

    assert fib_gen() == 0
    assert fib_gen() == 1
    assert fib_gen() == 1
    assert fib_gen() == 2
    assert fib_gen() == 3
    assert fib_gen() == 5

# Test 12-17: Functionality of function_call_counter with global dictionary
def test_function_call_counter_global():
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
    div(4, 2)

    assert global_call_counts['add'] == 2
    assert global_call_counts['mul'] == 1
    assert global_call_counts['div'] == 1

# Test 18-23: Functionality of function_call_counter with different dictionaries
def test_function_call_counter_different_dicts():
    call_counts_1 = {'add': 0, 'mul': 0, 'div': 0}
    call_counts_2 = {'add': 0, 'mul': 0, 'div': 0}

    @function_call_counter(call_counts_1)
    def add(a, b):
        return a + b

    @function_call_counter(call_counts_1)
    def mul(a, b):
        return a * b

    @function_call_counter(call_counts_2)
    def div(a, b):
        return a / b

    add(1, 2)
    add(3, 4)
    mul(2, 3)
    div(4, 2)
    div(6, 3)

    assert call_counts_1['add'] == 2
    assert call_counts_1['mul'] == 1
    assert call_counts_1['div'] == 0
    assert call_counts_2['add'] == 0
    assert call_counts_2['mul'] == 0
    assert call_counts_2['div'] == 2

if __name__ == '__main__':
    pytest.main()
