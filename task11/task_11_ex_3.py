"""
Task 3

Implement a decorator `call_once` which runs `sum_of_numbers` function once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments.

Example:
@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))

>>> 55

print(sum_of_numbers(999, 100))

>>> 55

print(sum_of_numbers(134, 412))

>>> 55
"""
from functools import wraps
from typing import Callable, Any


def call_once(func: Callable[..., int]) -> Callable[..., Any]:
    """The decorator, which runs function once and caches the result.
    All consecutive calls to this function should return cached result
    no matter the arguments."""

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        wrapper.result = getattr(wrapper, "result", None)
        if wrapper.result is None:
            wrapper.result = func(*args)
        return wrapper.result

    return wrapper


@call_once
def sum_of_numbers(a: int, b: int) -> int:
    """Sum two numbers"""
    return a + b


if __name__ == '__main__':
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
