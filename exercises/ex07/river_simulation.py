"""File used to call River and start simulation"""

from exercises.ex07.river import River

__author__: str = "730763577"


my_river: River = River(num_fish=10, num_bears=2)

my_river.view_river()
