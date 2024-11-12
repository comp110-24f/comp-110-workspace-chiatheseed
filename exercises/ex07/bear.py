"""File to define Bear class."""

__author__: str = "730763577"


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        """Creates new Bear object"""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increases age of each bear by 1 and decreases hunger score by 1 each day"""

        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increases hunger score of bear by num_fish eaten each day"""

        self.hunger_score += num_fish
        return None
