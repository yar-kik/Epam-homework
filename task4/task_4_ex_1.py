"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""
from argparse import ArgumentParser


def swap_quotes(string: str) -> str:
    """
    Function which receives a string and replaces all " symbols with '
    and vise versa
    @param string: string to replace symbols
    @return: modified string
    """
    new_string = ''
    for symbol in string:
        if symbol == '"':
            symbol = "'"
        elif symbol == "'":
            symbol = '"'
        new_string += symbol
    return new_string


def main() -> None:
    """
    Main function
    @return: None
    """
    parser = ArgumentParser()
    parser.add_argument("string", type=str)
    args = parser.parse_args()
    print(swap_quotes(args.string))


if __name__ == '__main__':
    main()
