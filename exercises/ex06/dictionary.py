"""Working extensively with dictionaries!"""

__author__ = "730763577"


# removing elements: dict.pop(key) + it returns the value


def invert(inputdict: dict[str, str]) -> dict[str, str]:
    """function inverts keys and values of input dict"""

    returndict: dict[str, str] = {}
    # houses the inverted dict
    # is OUTSIDE the for in loop

    for key in inputdict:
        new_value: str = key
        # create a variable that holds new value (current key)

        new_key: str = inputdict[key]
        # create a variable that holds new key (current value)

        instance: int = 0
        # count number of times key appears in dictionary
        # uses instance to raise KeyError

        for key in inputdict:
            if new_key == inputdict[key]:
                instance += 1

        if instance > 1:
            # if instance of key appears more than once, raises KeyError
            raise KeyError(
                "Can't invert! There is more than one of the same inverted key!"
            )

        returndict[new_key] = new_value
        # variable new_key is set equal to old value
        # new_key: str = dict.pop(key) does not work; can't mutate dict during loop iteration

    # print(returndict) - works!!
    return returndict


# INVERT - DONE
# inverts key and value
# can't have two of the same values -> if do, raise KeyError
# syntax for creating a new key AND updating one: dict[key] = [value]
# len(dict)
# for loops work the same! (for key in dict: ...)


def favorite_color(color_dict: dict[str, str]) -> str:
    """takes dict of names and favorite color and returns the color that appears most frequently"""
    # if tie, returns color that shows up first

    color_freq: dict[str, int] = {}
    # blank dict to store color as key and color count as value

    for names in color_dict:
        # for in loop to eval all values in input dict

        var_color: str = color_dict[names]
        # variable that is the current color in loop

        if var_color in color_freq:
            # if said color already exists, add one to value count
            color_freq[var_color] += 1
        else:
            # else, create new key/value pair and set equal to 1
            color_freq[var_color] = 1

    # result: a dict that contains color as key and count as value

    max: int = 0
    # okay to set as 0, as there won't be negatives!
    most_color: str = ""
    # variable to hold key that is paired to max, the value

    for color in color_freq:
        if color_freq[color] > max:
            # if current color freq is larger than max, set max to new largest freq
            max = color_freq[color]
            most_color = color

    return most_color

    # print(color) - works!!!


# FAV COLOR - DONE
# given dictionary of names and fav color, name unimportant
# returns most popular color
# should have a color count variable
# make a new dictionary to keep track of color frequency;
# key is color name, value is color count
# returns the color name using for loop
# max is a variable

# ideas that WON'T work:
# make lists for each color, each list value is the key name, list name is the color?
# then find the list with the longest length and return list name???


def count(input_list: list[str]) -> dict[str, int]:
    """produces a dict where each key is a unique value in the list and each
    value is the frequency of that value in the list"""

    return_dict: dict[str, int] = {}
    # first, create an empty dict to store result

    for num in input_list:
        if num in return_dict:
            # if item is already in dict, increase value associated w/ key by 1
            return_dict[num] += 1
        else:
            # if the item not found in dict, assign initial count of 1
            return_dict[num] = 1

    return return_dict


def alphabetizer(grouplist: list[str]) -> dict[str, list[str]]:
    """produces a dict where each key is unqiue letter in alphabet and value is a list of words beginning w that letter"""

    wordlist: list[str] = []
    # list that will store words to be added to dict value

    returndict: dict[str, list[str]] = {}
    # dict where key is first letter of word list and value is the word list

    for word in grouplist:
        letter: str = word[0].lower()
        # letter is a variable that holds the lowercase first letter of the word

        if letter in returndict:
            wordlist.append(word)
            returndict[letter] += wordlist

            wordlist = []
            # resets list to be empty for next for in loop

        else:
            wordlist = [word]
            returndict[letter] = wordlist
            wordlist = []
            # resets list to be empty for next for in loop

    return returndict


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """update an attendance dictionary given a day and student - dict is mutated but returns None"""

    studentlist: list[str] = []

    for weekday in attendance_log:
        # weekday is the key and list of students is the value

        if day == weekday:
            studentlist.append(student)
            attendance_log[weekday] += studentlist

            studentlist = []
        # if day already exists in attendance log, simply appends student to the value list
        else:
            studentlist = [student]
            attendance_log[day] = studentlist
            studentlist = []

    return None
