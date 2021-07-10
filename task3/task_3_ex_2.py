"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
from argparse import ArgumentParser

roman_numerals = {
    "I": 1,
    'IV': 4,
    "V": 5,
    'IX': 9,
    "X": 10,
    'XL': 40,
    "L": 50,
    'XC': 90,
    "C": 100
}


def from_roman_numerals(N: str) -> int:
    """
    Function to convert Roman numeral to Arabic numeral
    @param N: string with Roman numeral
    @return: integer of Arabic numeral
    """
    not_allowed_symbols = any([element for element in N
                               if element not in roman_numerals])
    if not_allowed_symbols or (len(N) > 1 and N.startswith('C')):
        raise ValueError
    result = 0
    i = 0
    while i < len(N):
        if i + 1 < len(N) and N[i:i + 2] in roman_numerals:
            result += roman_numerals[N[i:i + 2]]
            i += 2
        else:
            result += roman_numerals[N[i]]
            i += 1
    return result


def main() -> None:
    """
    Main function
    @return: None
    """
    parser = ArgumentParser()
    parser.add_argument('N', type=str, help="Roman numeral to convert")
    args = parser.parse_args()
    print(from_roman_numerals(args.N))


if __name__ == "__main__":
    main()
