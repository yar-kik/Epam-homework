"""
Implement function count_letters, which takes string as an argument and
returns a dictionary that contains letters of given string as keys and a
number of their occurrence as values.

Example:
print(count_letters("Hello world!"))
Result: {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

Note: Pay attention to punctuation.
"""


def count_letters(given_string: str) -> dict:
    """Takes string as an argument and returns a dictionary that contains
    letters of given string as keys and a number of their occurrence
    as values."""
    if not isinstance(given_string, str):
        raise TypeError
    given_string = "".join([i for i in given_string if i.isalpha()])
    result = dict()
    for char in given_string:
        result[char] = result.get(char, 0) + 1
    return result
