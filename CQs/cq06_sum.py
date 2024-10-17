"""Summing the elements of a list using different loops"""

__author__ = "730763577"


def w_sum(vals: list[float]) -> float:
    """takes input as list[float] and returns sum of all elems w/ while loop"""

    if len(vals) == 0:
        return 0.0
    # if list is empty, returns 0.0

    index: int = 0
    sumelem: float = vals[index]
    index += 1
    # index as separate variable will track index for while loop

    while index < len(vals):
        sumelem += vals[index]
        index += 1
        # prevents while loop from running infinitely
    return sumelem


def f_sum(vals: list[float]) -> float:
    """does the same thing as w_sum but using for loop!"""

    if len(vals) == 0:
        return 0.0
    # if list is empty, returns 0.0

    sumelem: float = 0.0

    for floats in vals:
        # for loops don't need to use index variable!
        sumelem += floats
    return sumelem


def f_range_sum(vals: list[float]) -> float:
    """does the same thing as f_sum but using for ... in range(...) loop!"""

    if len(vals) == 0:
        return 0.0
    # if list is empty, returns 0.0

    sumelem: float = 0.0

    for floats in range(0, len(vals)):
        # for in loops give more specificity to range!
        sumelem += vals[floats]
        # Note! it is += vals[floats] because floats is the INDEX
        # if you just did += floats, it would always add up to 3.0 because range counts the index

    return sumelem
