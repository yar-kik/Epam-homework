"""
Task04_1_2
Write `is_palindrome` function that checks whether a string is a palindrome or not
Returns 'True' if it is palindrome, else 'False'

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

Note:
Usage of any reversing functions is prohibited.
The function has to ignore special characters, whitespaces and different cases
Raise ValueError in case of wrong data type
"""
from argparse import ArgumentParser


def is_palindrome(string: str) -> bool:
    """
    Check whether a string is a palindrome or not
    @param string: string to check
    @return: bool
    """
    if not isinstance(string, str):
        raise ValueError
    string = string.lower()
    # remove special character and whitespaces:
    string = "".join(filter(str.isalpha, string))
    reversed_string = ""
    for character in string:
        reversed_string = character + reversed_string
    return string == reversed_string


def main() -> None:
    """
    Main function
    @return: None
    """
    parser = ArgumentParser()
    parser.add_argument("string", type=str)
    args = parser.parse_args()
    print(is_palindrome(args.string))


if __name__ == '__main__':
    main()

