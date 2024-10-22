"""implementing more list utility functions!"""

__author__ = "730763577"


def only_evans(input_list: list[int]) -> list[int]:
    """returns only elements of input list that are even w/o mutating input list"""

    # new list that holds even elems
    evens_list: list[int] = []

    # for in loop iterates over each elem in the input list
    for i in input_list:
        # if even, append it to the evens_list
        if i % 2 == 0:
            evens_list.append(i)
    return evens_list


# testing only_evens function
# print(only_evans(input_list=[4, 4, 4]))


def sub(alist: list[int], idxs: int, idxe: int) -> list[int]:
    """generates a subset list of input list, between specified start idx + end idx - 1"""
    # will not mutate input list
    # start index is inclusive, end index is not inclusive

    # new subset list generated from inputs, this is returned
    subset_list: list[int] = []

    # CHECKS
    # If start index is neg, start from beginning of list.
    if idxs <= 0:
        idxs = 0
        # is working, returns 0

    # If end index is greater than len of list, end w the end of list.
    if idxe > len(alist):
        idxe = len(alist)
        # is working, returns 4

    # If len of list is 0, start is greater than/equal to len of list, or end is at most 0, return empty list.
    if len(alist) == 0 or idxs >= len(alist) or idxe <= 0:
        subset_list = []
        return subset_list
        # is working, returns []

    for i in range(idxs, idxe):
        subset_list.append((alist[i]))

    # fixed an error: return should be OUTSIDE for in loop
    # if it's not it only returns one elem in list before exiting funct
    return subset_list


# testing sub function
# print(sub(alist=[10, 20, 30, 40], idxs=1, idxe=3))


def add_at_index(input_list: list[int], add_elem: int, idx_add: int) -> None:
    """mutates input list to place a new element at a chosen index"""

    # CHECKS
    if idx_add < 0 or idx_add > len(input_list):
        raise IndexError("Index is out of bounds for the input list")

    # front part of list split
    lista: list[int] = []
    # back part of list split
    listb: list[int] = []

    for i in range(0, idx_add):
        lista.append(input_list[i])
    for i in range(idx_add, len(input_list)):
        listb.append(input_list[i])

    lista.append(add_elem)

    for i in listb:
        lista.append(i)

    input_list = []

    for i in lista:
        input_list.append(i)

    print(input_list)


# testing add at index function
# add_at_index(input_list=[10, 9, 8, 7, 5], add_elem=6, idx_add=4)


# len(input_list)


# PLAN OF ACTION
# we split the list into two lists by making for in loops with the range of 0, idx and idx+1, len(list)
# append into two separate lists under each for in loop
# add elem at end of first list
# join 2 lists together again by for in looping twice?

# first int is the element to add
# second int is the index at which it is added

# 1,2,3,5 -> 4,3 -> 1,2,3,4,5


# ADD AT INDEX
# append smth to the end of the list
# then shift everything to the right of the index to make space for input elem
# before you can insert new elem at correct index