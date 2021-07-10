"""Implement a function `most_common_words(file_path: str, top_words: int) -> list`
which returns most common words in the file.
<file_path> - system path to the text file
<top_words> - number of most common words to be returned

Example:

print(most_common_words(file_path, 3))
>>> ['donec', 'etiam', 'aliquam']
> NOTE: Remember about dots, commas, capital letters etc.
"""
import re
from collections import Counter


def most_common_words(file_path: str, top_words: int) -> list:
    """Returns most common words in the file."""
    with open(file_path, 'r') as file:
        raw_text = file.read()
    text = raw_text.lower()
    all_worlds = re.findall(r"\w+", text)
    counter = Counter(all_worlds)
    most_common = [value for value, count in counter.most_common(top_words)]
    return most_common
