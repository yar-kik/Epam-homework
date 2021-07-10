"""
Implement a function get_longest_word(s: str) -> str which returns the
longest word in the given string. The word can contain any symbols
except whitespaces (`,\n,\t and so on). If there are multiple longest
words in the string with a same length return the word that occurs first.

Example:
get_longest_word('Python is simple and effective!')
#output: 'effective'
get_longest_word('Any pythonista like namespaces a lot.')
#output: 'pythonista'

Note:
Raise ValueError in case of wrong data type
Usage of 're' library is required.
"""
import re


def get_longest_word(given_string: str):
    """Returns the longest word in the given string."""
    if not isinstance(given_string, str):
        raise ValueError
    all_words = re.findall(r"\w+", given_string)
    sorted_word = sorted(all_words, key=len, reverse=True)
    return sorted_word[0]

