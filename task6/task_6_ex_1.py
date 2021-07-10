"""
Implement function combine_dicts, which receives a changeable
number of dictionaries (keys - letters, values - integers)
and combines them into one dictionary.

Dict values should be summarized in case of identical keys.

Example:
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

combine_dicts(dict_1, dict_2)
Result: {'a': 300, 'b': 200, 'c': 300}

combine_dicts(dict_1, dict_2, dict_3)
Result: {'a': 600, 'b': 200, 'c': 300, 'd': 100}
"""
from typing import Dict


def combine_dicts(*args) -> Dict[str, int]:
    """
    Combine_dicts, which receives a changeable number of dictionaries
    (keys - letters, values - integers) and combines them into one dictionary.
    @param args: dicts to combine
    @return:
    """
    new_dictionary = {}
    for dictionary in args:
        for key in dictionary:
            if not key.isalpha() or len(key) > 1:
                raise KeyError
            if not isinstance(dictionary[key], int):
                raise ValueError
            if key not in new_dictionary:
                new_dictionary[key] = dictionary[key]
            else:
                new_dictionary[key] += dictionary[key]
    return new_dictionary

