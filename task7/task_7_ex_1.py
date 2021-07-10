"""
Develop Rectangle class with following content:
    2 private fields type of float `side_a` and `side_b` (sides А and В of the rectangle);
    One constructor with two optional parameters a and b (parameters specify rectangle sides). Side А of a rectangle
    defaults to 4, side В - 3. Raise ValueError if received parameters are less than or equal to 0;
    Method `get_side_a`, returning value of the side А;
    Method `get_side_b`, returning value of the side В;
    Method `area`, calculating and returning the area value;
    Method `perimeter`, calculating and returning the perimeter value;
    Method `is_square`, checking whether current rectangle is square or not. Returns True if the shape is square and
    False in another case;
    Method `replace_sides`, swapping rectangle sides.

Develop class ArrayRectangles, in which declare:
    Private attribute `rectangle_array` (list of rectangles);
    One constructor that creates a list of rectangles with length `n` filled with `None` and that receives an
    arbitrary amount of objects of type `Rectangle` or a list of objects of type `Rectangle` (the list must be
    unpacked inside the constructor so that there will be no nested arrays). If both objects and length are passed,
    at first creates a list with received objects and then add the required number of Nones to achieve the
    desired length. If `n` is less than the number of received objects, the length of the list will be equal to the
    number of objects;
    Method `add_rectangle` that adds a rectangle of type `Rectangle` to the array on the nearest free place and
    returning True, or returning False, if there is no free space in the array;
    Method `number_max_area`, that returns order number (index) of the first rectangle with the maximum area value
    (numeration starts from zero);
    Method `number_min_perimeter`, that returns order number (index) of the first rectangle with the minimum area value
    (numeration starts from zero);
    Method `number_square`, that returns the number of squares in the array of rectangles
"""


class Rectangle:
    def __init__(self, a: float = 4, b: float = 3):
        if a <= 0 or b <= 0:
            raise ValueError
        self.__side_a = a
        self.__side_b = b

    def area(self) -> float:
        """Calculating and returning the area value."""
        return self.__side_a * self.__side_b

    def perimeter(self) -> float:
        """Calculating and returning the perimeter value."""
        return 2 * (self.__side_a + self.__side_b)

    def get_side_a(self) -> float:
        """Returning value of the side А."""
        return self.__side_a

    def get_side_b(self) -> float:
        """Returning value of the side В."""
        return self.__side_b

    def is_square(self) -> bool:
        """Checking whether current rectangle is square or not."""
        return self.__side_a == self.__side_b

    def replace_sides(self) -> None:
        """Swapping rectangle sides."""
        self.__side_a, self.__side_b = self.__side_b, self.__side_a

    def __repr__(self) -> str:
        return f"Rectangle {self.__side_a}x{self.__side_b}"


class ArrayRectangles:
    def __init__(self, *args, n: int = 0):
        rectangle_array = []
        for rectangle in args:
            if isinstance(rectangle, Rectangle):
                rectangle_array.append(rectangle)
            else:
                rectangle_array.extend(rectangle)
        if len(rectangle_array) < n:
            rectangle_array += [None] * (n - len(rectangle_array))
        self.__rectangle_array = rectangle_array

    def add_rectangle(self, new_rectangle: Rectangle) -> bool:
        """adds a rectangle of type `Rectangle` to the array on the nearest
        free place and returning True, or returning False, if there is no
        free space in the array."""
        for i, rectangle in enumerate(self.__rectangle_array):
            if rectangle is None:
                self.__rectangle_array[i] = new_rectangle
                return True
        return False

    def number_max_area(self) -> int:
        """Returns order number (index) of the first rectangle with
        the maximum area value."""
        max_area = 0
        max_area_index = 0
        for i, rectangle in enumerate(self.__rectangle_array):
            if rectangle is not None and rectangle.area() > max_area:
                max_area = rectangle.area()
                max_area_index = i
        return max_area_index

    def number_min_perimeter(self) -> int:
        """returns order number (index) of the first rectangle with
        the minimum perimeter value."""
        min_perimeter = float("inf")
        min_perimeter_index = 0
        for i, rectangle in enumerate(self.__rectangle_array):
            if rectangle is not None and rectangle.perimeter() < min_perimeter:
                min_perimeter = rectangle.perimeter()
                min_perimeter_index = i
        return min_perimeter_index

    def number_square(self) -> int:
        """Returns the number of squares in the array of rectangles."""
        number_square = 0
        for rectangle in self.__rectangle_array:
            if rectangle is not None and rectangle.is_square():
                number_square += 1
        return number_square

    def __repr__(self) -> str:
        return str(self.__rectangle_array)
