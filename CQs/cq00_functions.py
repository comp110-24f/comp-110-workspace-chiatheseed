"""Challenge question number one! Mimic, main"""

__author__ = "730763577"


def mimic(message: str) -> str:
    """Mimic will return you input back to you"""
    return message


def main() -> None:
    """Main is only going to print the result of calling mimic"""
    # None MUST be capitalized
    print(mimic(message=input("What is your message?")))
    # the above is called a nested function call !!!
    # this is bc the result (aka return value) of mimic
    # is then passed as an argument to print
    # More on input:
    # argument - whatever message you want displayed
    # return value - str of whatever user has typed


if __name__ == "__main__":
    main()
"""the first line is a special kind of statement 
called a conditional statement"""
# If you run this in the "Run", the indented code beneath "if" is evaluated
# If you load this in "Interact", the code beneath is not run!
# Gives us the best of both worlds
