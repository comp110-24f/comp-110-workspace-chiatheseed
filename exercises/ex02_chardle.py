"""EX02 - Chardle - A cute step toward Wordle."""

# This exercise prompts the user for a five-character word and a single letter.
# You will then test to see which indices of the word match the single letter.

__author__: str = "730763577"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """user types in word and it must be 5 letters long
    function verifies length"""

    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        # print(word)
        return word
    # input word will show up in terminal
    else:
        print("Error: Word must contain 5 characters.")
        # if word is more than 5 char, error returns in terminal
        exit()
        # function ends to prevent it returning faulty input


# input_word()
# we don't need to call function since main does that


def input_letter() -> str:
    """user types in a letter used for indicing
    function verifies length"""

    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        # print(letter)
        return letter
    # letter must be 1
    else:
        print("Error: Character must be a single character.")
        # if char is not 1 length long, error returned in terminal
        exit()
        # function ends to prevent it returning faulty input


# input_letter()
# we don't need to call function since main does that


def contains_char(word: str, letter: str) -> None:
    """function checks if the input character matches
    any of the characters within the input word"""

    count: int = 0
    # count will keep track on # of instances letter matches indice

    print("Searching for " + letter + " in " + word)
    if letter == word[0]:
        # function will compare letter with each letter in word
        print(letter + " found at index 0")
        # print if it is found at what index
        count += 1
        # if there is a match, count will increase by 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count += 1

    # to acheive exactly what is asked:
    # "No instances" instead of "0 instances"
    # "1 instance" instead of "1 instances"
    if count == 1:
        print(f"1 instance of {letter} found in {word}")
    elif count > 0:
        print(f"{count} instances of {letter} found in {word}")
    else:
        print(f"No instances of {letter} found in {word}")


# contains_char(word="magic", letter="g")
# we don't need to call function since main does that

if __name__ == "__main__":
    main()
