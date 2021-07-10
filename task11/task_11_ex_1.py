"""
1) Find a way to call inner_function without moving it from inside of enclosed_function.
2) Use the solution made in the function `enclosing_function_1` as a basis. Modify ONE LINE (do not remove or add a
new one) in inner_function to make it print variable 'a' from global scope.
3) Use the solution made in the function `enclosing_function_1` as a basis. Modify ONE LINE (do not remove or add a
new one) in inner_function to make it print variable 'a' form enclosing function.


Each function call from `main` should print a string. You CANNOT change the `main` function. You CANNOT change the
content of strings.
"""

a = 'I am global variable!'


def enclosing_function():
    """
    Call inner_function without moving it outside of enclosed_function.
    """
    a = 'I am variable from enclosed function!'

    def inner_function():
        a = 'I am local variable!'
        print(a)
    inner_function()

def print_global():
    """
    Use the solution made in the function `enclosing_function_1` as a basis.
    Modify one line (do not remove or add a new one) in inner_function to make
    it print variable `a` from global scope.
    """
    a = 'I am variable from enclosed function!'

    def inner_function():
        global a
        print(a)
    inner_function()

def print_enclosed():
    """
    Use the solution made in the function `enclosing_function_1` as a basis.
    Modify one line (do not remove or add a new one) in inner_function to make it print variable `a` from enclosing
    scope.
    """
    a = 'I am variable from enclosed function!'

    def inner_function():
        nonlocal a
        print(a)
    inner_function()

def main():
    enclosing_function()
    print_global()
    print_enclosed()


if __name__ == '__main__':
    main()
