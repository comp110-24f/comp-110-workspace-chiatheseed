"""Coding wordle! This is hard..."""

__author__: str = "730763577"


def input_guess(correct_length: int) -> str:
    """user types in word and it must be # of letters of secret word length
    function verifies length"""
    guess: str = input(f"Enter a {correct_length} character word: ")

    while len(guess) != correct_length:
        if len(guess) == correct_length:
            return guess
        # input word will show up in terminal
        else:
            guess = input(f"That wasn't {correct_length} chars! Try again: ")
            # if word is more than correct_length, error returns in terminal
            exit()
            # function ends to prevent it returning faulty input
    return guess


print(input_guess(correct_length=5))

# must use while loop
# parameter int - value of # of char gues should contain
# ^ corresponds to length of secret word
# should return guessed word
