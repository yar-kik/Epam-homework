"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""
from typing import List


def split_alternative(string: str, delimiter: str = ' ') -> List[str]:
    """
    Split string (as built-in function)
    @param delimiter: default is whitespace
    @param string: string to split
    @return: split string
    """
    if not isinstance(string, str):
        raise ValueError
    split_string = []
    chunk = ''
    for character in string:
        if character == delimiter:
            if chunk:
                split_string.append(chunk)
            chunk = ''
        else:
            chunk += character
    if chunk:
        split_string.append(chunk)
    return split_string
