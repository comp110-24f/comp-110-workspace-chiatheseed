"""Mutating functions."""

__author__: str = "730763577"


def manual_append(list1: list[int], appendx: int) -> None:
    """mutates input by appending int paramenter to end of list paramenter"""

    list1.append(appendx)
    return None


def double(list2: list[int]) -> None:
    """mutates input by mult every element in the list parameter by 2"""

    index: int = 0

    while index < len(list2):
        list2[index] = list2[index] * 2
        # replacing each element in list with element * 2
        index += 1

    return None


# global variables
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
# What will be printed for list_1? What will be printed for list_2?
# Test yourself and then run in repl or trailhead!
