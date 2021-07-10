"""
Create function sum_geometric_elements, determining the sum of the first elements of a decreasing geometric
progression of real numbers with a given initial element of a progression `a` and a given progression step `t`,
while the last element must be greater than a given `lim`. `an` is calculated by the formula (an+1 = an * t), 0<t<1
Function must return float and round the answer to three decimal places using round().
Check the parameter `t` and raise a ValueError if it does not satisfy the inequality 0<t<1.
`a` and `lim` must be greater than 0, otherwise raise a ValueError.

Example,
For a progression, where a1 = 100, and t = 0.5, the sum of the first elements, grater than alim = 20, equals to
100+50+25 = 175
"""


def sum_geometric_elements(a: float, t: float, lim: float) -> float:
    """
    Calculates the sum of the first elements of a decreasing geometric
    progression of real numbers.
    @param a: Initial element of a progression.
    @param t: Progression step.
    @param lim: minimal value of geometric progression
    @return: sum of elements geometric progression
    """
    if 0 >= t or t >= 1 or a <= 0 or lim <= 0:
        raise ValueError
    progression_elements = []
    element = a
    i = 0
    while element * t > lim:
        element = a * t ** i
        progression_elements.append(element)
        i += 1
    result = sum(progression_elements)
    return round(result, 3)

