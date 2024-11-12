"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__: str = "730763577"


class River:
    """Defines class River."""

    # what day of the river’s lifecycle ur modeling
    day: int
    # river's fish population
    fish: list[Fish]
    # river's bear population
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """Creates a new river with num_fish Fish and num_bears Bears."""
        self.day = 0
        self.fish = []
        self.bears = []

        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages of each fish and bear -> if above age req, adds them to lists."""
        # new fish list to move surviving fish over
        new_fish: list[Fish] = []
        # new bear list to move surviving bears over
        new_bear: list[Bear] = []

        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)

        for bear in self.bears:
            if bear.age <= 5:
                new_bear.append(bear)

        self.fish = new_fish
        self.bears = new_bear

        return None

    def remove_fish(self, amount: int):
        """Removes an amt of fish (amount) from River."""
        # removes FRONTMOST fish; Fish at idx 0

        # new fish list to move fish NOT being removed
        """keep_fish: list[Fish] = []

        for x in range(amount - 1, len(self.fish)):
            keep_fish.append(self.fish[x])

        self.fish = keep_fish"""
        for i in range(0, amount):
            self.fish.pop(i)

        return None

    def bears_eating(self):
        """Updates river simulation if and when bear eats."""
        # if there are at least 5 fish in the river, bear eats 3 fish; river looses 3 fish
        for bear in self.bears:
            # Had an issue: didn't use a for loop
            if len(self.fish) >= 5:
                self.remove_fish(amount=3)
                # wasn't working at first
                # issue was I used Bear.eat instead of bear.eat
                bear.eat(num_fish=3)
        return None

    def check_hunger(self):
        """Removes bears whose hunger score reaches negative."""
        # new bear list to move surviving bears over
        keep_bear: list[Bear] = []

        for bear in self.bears:
            if bear.hunger_score >= 0:
                # which one is correct? Bear() or self.bears[x]?
                keep_bear.append(bear)

        self.bears = keep_bear
        return None

    def repopulate_fish(self):
        """Adds 4 fish for every fish pair."""
        # if num of fish is even -> each fish is paired up

        if len(self.fish) % 2 == 0:
            for _ in range(0, int((len(self.fish) // 2) * 4)):
                self.fish.append(Fish())
        elif (len(self.fish) - 1) % 2 == 0:
            for _ in range(0, int(((len(self.fish) - 1) // 2) * 4)):
                self.fish.append(Fish())

        return None

    def repopulate_bears(self):
        """Adds 1 bear for every bear pair."""
        # if num of bears is even -> each bear is paired up
        if len(self.bears) % 2 == 0:
            for _ in range(0, int(len(self.bears) // 2)):
                self.bears.append(Bear())
        elif (len(self.bears) - 1) % 2 == 0:
            for _ in range(0, int(len(self.bear) // 2)):
                self.bear.append(Bear())

        return None

    def view_river(self):
        """Prints the day # and fish and bear population."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

        return None

    def one_river_day(self):
        """Simulates one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one river day seven times."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None
