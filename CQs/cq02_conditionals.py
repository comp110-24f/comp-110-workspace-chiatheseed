"""Practice w conditionals, local variables, and user input to create a simple number guessing game"""

__author__: str = "730763577"


def guess_a_number() -> None:
    """This funct calls players to input a number,
    then evaluates if they guessed right or not."""

    secret: int = 7
    # secret is the secret number players are guessing
    x = input("Guess a number: ")
    # x is a local variable and is what the player guesses
    print("Your guess was " + x)
    if int(x) == secret:
        print("You got it!")
    elif int(x) < secret:
        # x must be converted into an int before comparing it with secret, another int
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
