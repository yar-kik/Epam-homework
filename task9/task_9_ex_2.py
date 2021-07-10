"""
Write a function that checks whether a string is a palindrome or not.
Return 'True' if it is a palindrome, else 'False'.

Note:
Usage of reversing functions is required.
Raise ValueError in case of wrong data type

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
"""


def is_palindrome(test_string: str) -> bool:
    """Checks whether a string is a palindrome or not."""
    if not isinstance(test_string, str):
        raise ValueError
    test_string = test_string.lower()
    test_string = "".join(filter(str.isalnum, test_string))
    return test_string == "".join(reversed(test_string))
