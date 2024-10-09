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
    # accounts for evaluating empty lists

    index: int = 0
    maxi: int = list[0]
    # variable used to hold current max int in list
    # set equal to list[0] to account for negatives!
    index = 1

    while index < (len(list)):
        if list[index] > maxi:
            # if current elem in list is bigger than maxi, set maxi equal to it
            maxi = list[index]
        index += 1
    return maxi


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Evals two lists[int], returns True if every element at every index is equal in both"""

    index: int = 0

    if len(list1) != len(list2):
        return False
        # first eval if len of both lists are the same length
        # even if elem at same indices are equal, size must be equal first
    elif len(list1) == len(list2):
        while index < len(list1):
            if list1[index] == list2[index]:
                index += 1
            else:
                # if elem at index n are not equal, returns False and immediately exits
                return False
    return True
    # will only return True if all elems and all indices are equal and exits while loop


# IS EQUAL
# should not assume len of each list is equal - deep equality
# 2 separate lists on heap may be distinct, but deeply equal if what they are is equal in essence
# compares 2 lists, if lists equal - True, else - False


def extend(list1: list[int], list2: list[int]) -> None:
    """Mutates 1st list[int] by appending the second list’s values to the end of it"""

    index: int = 0
    while index < len(list2):
        list1.append(list2[index])
        index += 1


# print(extend(list1=[1, 3, 5], list2=[2, 4, 6]))
