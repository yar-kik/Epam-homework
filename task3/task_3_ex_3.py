"""
Write a Python-script that:
1. Searches for files by a given pattern (pattern can include: *, ?)
2. Displays the search result
3. Gets access rights for each file that is found and displays the result

The script should have 2 obligatory functions:
- finder - a generator function searches for files by a given pattern
 in a given path returns an absolute path of a found file.
- display_result - displays founded files and files' permission
by a given list of absolute paths (You can find an example below).

Example call:
python task_3_ex_3.py /usr/bin -p '?ython*'

Example result:
...
/usr/bin/python3.6m -rwxr-xr-x
/usr/bin/python3.7m -rwxr-xr-x
Found 12 file(s).

Note: use of glob module is prohibited.

Hint: use os.walk, stat, fnmatch
"""
from argparse import ArgumentParser
from fnmatch import filter
from stat import filemode
from os import walk, stat
from os.path import join
from typing import List


def finder(path: str, pattern: str) -> list:
    """Searches for files by a given pattern.

    :param path: Absolute path for searching.
    :param pattern: Can consist *, ?.
    :return: absolute path of found file.
    """
    file_paths = []
    for root, dirs, files in walk(path):
        for filename in filter(files, pattern):
            file_paths.append(join(root, filename))
    return file_paths


def display_result(file_paths: List[str]) -> None:
    """Displays founded file paths and file's permissions."""
    for file_path in file_paths:
        file_permission = filemode(stat(file_path).st_mode)
        print(file_path, file_permission)
    print(f"Found {len(file_paths)} file(s).")


def main():
    parser = ArgumentParser(
        description="Searches for files by a given pattern (pattern can "
                    "include: *, ?). It also displays founded file paths "
                    "and file's permissions.")
    parser.add_argument('path', type=str,
                        help="Absolute path for searching")
    parser.add_argument('-p', type=str,
                        help="Pattern, that can consist '*', '?'")
    args = parser.parse_args()
    display_result(finder(args.path, args.p))


if __name__ == '__main__':
    main()
