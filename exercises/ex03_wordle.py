"""Coding wordle! This is hard..."""

__author__: str = "730763577"


def input_guess(correct_length: int) -> str:
    """function verifies input word length to be # of letters of secret word length"""
    guess: str = input(f"Enter a {correct_length} character word: ")
    # local variable guess is user input
    while len(guess) != correct_length:
        if len(guess) == correct_length:
            return guess
        # input word will show up in terminal, with help of print()
        else:
            guess = input(f"That wasn't {correct_length} chars! Try again: ")
            # if word is more than correct_length, returns error
            # exit()
    return guess


# print(input_guess(correct_length=5))

# INPUT_GUESS
# must use while loop
# parameter int - value of # of char gues should contain
# ^ corresponds to length of secret word
# should return guessed word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """funct tests each index of 1st parameter string to see if it matches 2nd parameter"""

    assert len(char_guess) == 1
    # asserts that 2nd argument has length of 1, if else, returns error
    index: int = 0
    # index tracks indicing

    while index < len(secret_word):
        if char_guess == secret_word[index]:
            return True
        else:
            index += 1
    # if char guess matches any element in secret word, returns True
    # after returning True, exits out of function
    return False
    # if none match, exits while loop and returns False


# print(contains_char(secret_word="abc", char_guess="c"))

# CONTAINS_CHAR
# 2 parameters, name descriptively:
# str indexed thru for occurence of 2nd para
# str, single char being searched for

# must work with word of any length = employ correct_length again
# if match found, return True
# if match not found, return False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# named constants to make program easier to read


def emojified(guess: str, secret: str) -> str:
    """returns str emojis to indicate char_guess is in the correct pos (green), wrong pos (yellow), or absent (white)"""

    assert len(guess) == len(secret)

    index: int = 0
    wordle_print: str = ""

    while index < len(secret):
        if guess[index] == secret[index]:
            wordle_print += f"{GREEN_BOX}"
        elif contains_char(secret_word=secret, char_guess=guess[index]) == True:
            wordle_print += f"{YELLOW_BOX}"
        else:
            wordle_print += f"{WHITE_BOX}"
        index += 1
    print(wordle_print)
    return wordle_print


# EMOJIFIED
# compares 2 strs: user guess and secret word
# should use while loop to test each index of secret word
# uses contains_char to determine use of Y/W boxes
# if char matches current index of guess -> green box
# if 1st scenario not met, check if char present in guess
# if so -> yellow box
# if neither met -> white box


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    # "state" of the game
    # variables needed to run the game
    turn_num: int = 1
    lose_statement: str = "X/6 - Sorry, try again tomorrow!"

    while turn_num <= 6:

        turn_statement: str = f"=== Turn {turn_num}/6 ==="
        win_statement: str = f"You won in {turn_num}/6 turns!"

        print(turn_statement)
        # displays turns out of 6 you're on
        if emojified(guess=input_guess(correct_length=len(secret)), secret=secret) == (
            f"{GREEN_BOX}" * len(secret)
        ):
            # first, input_guess verfies length of guess is corrent length
            # if so, guess is returned and becomes argument for emojified
            # emojified uses function contains_char to determine Y or W box
            # this is all within an IF statement testing if guess is completely right (6 green boxes)

            print(win_statement)
            # if above IF statement is eval True, win_statement prints with num of turns
            # exit()

        elif turn_num == 6:
            print(lose_statement)
        else:
            turn_num += 1

    """if turn_num == 7:
        print(lose_statement)   """


# MAIN
# while the user still has turns left and has not won yet:
# Print the current turn number in a format such as === Turn 1/6 ===
# Prompt the user for a guess, relying on your function input_guess to obtain a guess of the correct length.
# Codify the emoji results of the user’s guess versus the secret by making use of your emojified function. Print the resulting codified string.
# If the user’s guess is the secret, the user has won!
# Otherwise, move on to the next turn.

if __name__ == "__main__":
    main(secret="codes")
