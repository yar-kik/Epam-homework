"""
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
  Note: raise ValueError if there are less than two strings
4) characters of alphabet, that were not used in any string
  Note: use `string.ascii_lowercase` for list of alphabet letters

Note: raise TypeError in case of wrong data type

Examples,
```python
test_strings = ["hello", "world", "python", ]
print(chars_in_all(*test_strings))
>>> {'o'}
print(chars_in_one(*test_strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(chars_in_two(*test_strings))
>>> {'h', 'l', 'o'}
print(not_used_chars(*test_strings))
>>> {'q', 'k', 'g', 'f', 'j', 'u', 'a', 'c', 'x', 'm', 'v', 's', 'b', 'z', 'i'}
"""
import string
from functools import reduce
from itertools import combinations


def chars_in_all(*strings) -> set:
    """Return characters that appear in all strings."""
    if not all([isinstance(i, str) for i in strings]):
        raise TypeError
    common_chars = reduce(set.intersection, map(set, strings))
    return common_chars


def chars_in_one(*strings) -> set:
    """Return characters that appear in at least one string."""
    if not all([isinstance(i, str) for i in strings]):
        raise TypeError
    all_chars = reduce(set.union, map(set, strings))
    return all_chars


def chars_in_two(*strings) -> set:
    """Return characters that appear at least in two strings."""
    if not all([isinstance(i, str) for i in strings]):
        raise TypeError
    if len(strings) < 2:
        raise ValueError
    set_combinations = combinations(strings, 2)
    common_in_two = set()
    for set_pair in set_combinations:
        common_in_two |= reduce(set.intersection, map(set, set_pair))
    return common_in_two


def not_used_chars(*strings) -> set:
    """Return characters of alphabet, that were not used in any string."""
    if not all([isinstance(i, str) for i in strings]):
        raise TypeError
    all_chars = reduce(set.union, map(set, strings))
    not_used = set(string.ascii_lowercase) - all_chars
    return not_used
