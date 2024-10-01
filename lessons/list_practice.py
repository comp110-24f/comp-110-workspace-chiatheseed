"""Practice with creating lists!"""

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

# adding an item to a list
my_numbers.append(1.5)

# print(my_numbers)


game_points: list[int] = []

game_points.append(102)
game_points.append(86)
game_points.append(94)

# Subscription Notation/Indexing
# print(game_points[2])

# Saving as variable
last_game: int = game_points[2]

# Modifying list elements w/ Index
# (because lists are mutable,,,strings are not)
# game_points[1] = 72

# Getting the length
y: int = len(game_points)

# Removing item from list
# game_points.pop(1)
# .pop(index#ofitem)


# Practice!


def function(list_name: list[int]) -> int:
    """Function will loop over input and print every value"""
    index: int = 0
    while index < len(list_name):
        print(list_name[index])
        index += 1


function(list_name=game_points)
