"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:

    day: int
    "what day of the river’s lifecycle ur modeling"
    fish: list[Fish]
    "river's fish population"
    bears: list[Bear]
    "river's bear population"

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day = 0
        self.fish = []
        self.bears = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        # new bear list to move surviving bears over
        new_bear: list[Bear] = []

        # new fish list to move surviving fish over
        new_fish: list[Fish] = []

        for _ in range(0, len(self.fish)):
            if Fish.age <= 3:
                new_fish.append(Fish())

        for _ in range(0, len(self.bears)):
            if Bear.age <= 5:
                new_bear.append(Bear())

        self.fish = new_fish
        self.bear = new_bear

        return None

    def remove_fish(self, amount: int):

        return None

    def bears_eating(self):
        return None

    def check_hunger(self):
        return None

    def repopulate_fish(self):
        return None

    def repopulate_bears(self):
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
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
        # calls one river day seven times
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None
