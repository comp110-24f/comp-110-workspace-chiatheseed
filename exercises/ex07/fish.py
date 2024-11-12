"""File to define Fish class."""

__author__: str = "730763577"


class Fish:
    age: int

    def __init__(self):
        """Creates new Fish object"""
        self.age = 0
        return None

    def one_day(self):
        """Increases age of each fish by 1 each day"""
        self.age += 1
        return None
