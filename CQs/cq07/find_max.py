"""Find max function"""

__author__: str = "730763577"


def find_and_remove_max(input_list: list[int]) -> int:
    """finds, removes, returns the largest number in the input list."""

    # if list is empty, returns -1
    if len(input_list) == 0:
        return -1

    max: int = input_list[0]

    # identifies max value in list using for in loop
    for i in range(0, len(input_list)):
        if max <= input_list[i]:
            max = input_list[i]

    # variable for indexes in while loop
    index: int = 0

    # identifies when max occurs in list and removes it
    while index < len(input_list):

        if max == input_list[index]:
            # removes value at current index if it is equal to max
            input_list.pop(index)
        # read notes
        else:
            index += 1

    # I was stuck on this for a long time !!!

    # the issue: after popping index, list moves down and index 1 becomes index 0
    # if next int is also max, while loop will skip evaluating it
    # solution: should evaluate index 0 UNTIL it isn't equal to max !!!
    # this is were else comes in: only if max != list[index], will index +=1

    print(input_list)
    return max


"""
l = [1, 2, 3]
print(find_and_remove_max(l))"""
