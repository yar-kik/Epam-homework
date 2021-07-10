"""
Implement a function `sort_names(input_file_path: str, output_file_path: str)
-> None`, which sorts names from `file_path` and write them to a new file
`output_file_path`. Each name should  start with a new line as in
the following example:
Example:

Adele
Adrienne
...
Willodean
Xavier
"""


def sort_names(input_file_path: str, output_file_path: str) -> None:
    """Sorts names from `file_path` and write them to a new file
    `output_file_path`."""
    with open(f"{input_file_path}", 'r') as input_file, \
            open(f"{output_file_path}", 'w') as output_file:
        all_names = input_file.read().strip()
        names_list = all_names.split("\n")
        sorted_names = "\n".join(sorted(names_list)) + '\n'
        output_file.write(sorted_names)
