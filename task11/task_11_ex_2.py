"""
Implement a decorator remember_result which remembers last result of function it decorates
and prints it before next call.

@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result

sum_list("a", "b")
>>> "Last result = 'None'"
>>> "Current result = 'ab'"

sum_list("abc", "cde")
>>> "Last result = 'ab'"
>>> "Current result = 'abccde'"

sum_list(3, 4, 5)
>>> "Last result = 'abccde'"
>>> "Current result = '345'"
"""
from functools import wraps
from typing import Callable, Union


def remember_result(fn: Callable) -> Callable[..., Callable[..., str]]:
    """The decorator, which remembers last result of function it decorates
    and prints it before next call."""
    @wraps(fn)
    def wrapper(*args) -> Callable[..., str]:
        wrapper.last_result = getattr(wrapper, "last_result", None)
        print(f"Last result = '{wrapper.last_result}'")
        wrapper.last_result = fn(*args)
        return wrapper.last_result
    return wrapper


@remember_result
def sum_list(*args: Union[str, int]) -> str:
    """Sum values of the arguments into string."""
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result


if __name__ == '__main__':
    a = sum_list("a", "b")
    b = sum_list("abc", "cde")
    c = sum_list(3, 4, 5)
