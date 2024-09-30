"""Pract w functions"""

__author__: str = "730763577"

from random import randint

__author__: str = "730763577"


print(randint(1, 20))


def sum(num1: int, num2: int) -> int:
    """Return num1 + num2"""
    return num1 + num2


# Call the function
print(sum(num1=1, num2=100))  # <- 1 and 100 are arguments
# BUT the arguments can also be a function, such as num1=randint(1,10)
