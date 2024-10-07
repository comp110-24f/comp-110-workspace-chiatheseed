"""Implement algorithms to practice computational thinking"""

__author__: str = "730763577"


def all(list: list[int], num: int) -> bool:
    """checks if all ints in the list are the same as the input int"""

    index: int = 0

    while index < len(list):
        if list[index] != num:
            return False
        # if an element does not match, short circuits loop and returns False immediately
        else:
            index += 1
    return True
    # if all elements in list match int, exits while loop w/o returning False and returns True instead


def max(list: list[int]) -> int:
    """returns largest int in the list. if empty, returns ValueError"""

    if len(list) == 0:
        raise ValueError("max() arg is an empty List")

    index: int = 0
    maxelem: int = 0
    # variable used to hold current max int in list

    while index < (len(list) - 1):
        if list[index] < list[index + 1]:
            maxelem = list[index + 1]
        elif list[index] >= list[index + 1]:
            maxelem = list[index]
        index += 1
    return maxelem

def is_equal(list1: list[int], list2: list[int]) -> bool:


    # should not assume len of each list is equal - deep equality
        # 2 separate lists on heap may be distinct, but deeply equal if what they are is equal in essence
    # compares 2 lists, if lists equal - True, else - False 