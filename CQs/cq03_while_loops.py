"""Practice with while loop to iterate over a string!"""

__author__: str = "730763577"


def num_instances(phrase: str, search_char: str) -> int:
    """function should return count occurences of
    search_char in phrase, is case sensitive"""
    count: int = 0
    # count is number of matching characters found
    index: int = 0
    # index is index of phrase
    while index < len(phrase):
        # index should be less than length of phrase
        if search_char == phrase[index]:
            count += 1
        # else is not required
        index += 1
        # add 1 to index after each loop to keep it moving
    print(count)
    # shows number of matching characters found in trailhead/terminal
    return count


num_instances(phrase="I want to try med deli really badly", search_char="e")
# specific phrase and character to search for
print(num_instances)
