"""Writing a program to help plan a cozy tea party! 
The program will calc the # of tea bags, treats, and expected
cost of the party."""

__author__: str = "730763577"


def main_planner(guests: int) -> None:
    """Calls each func below with input from user
    and prints output"""
    # common pattern for “main” functions:
    # they orchestrate the execution of a program
    # and produce output
    # but they do not return a value
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # guests is parameter in function, do not call main_planner with main_planner lol
    print("Tea Bags: " + str((tea_bags(people=guests))))
    # keyword people=guests
    print("Treats: " + str(treats(people=guests)))
    # keyword people=guests
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # keyword people=guests and tea_count and treat_count are connected to other functions


def tea_bags(people: int) -> int:
    """A func to compute # of tea
    bags needed based on # of guests."""
    return people * 2


def treats(people: int) -> int:
    """A func to compute # of treats
    needed based on # of teas guests
    are expecting to drink"""
    return int(tea_bags(people=people) * 1.5)  # calls tea_bags
    # converts to int before returning
    # we're calling tea_bags, so keyword argument is people=people


def cost(tea_count: int, treat_count: int) -> float:
    """A func to compute combined cost of tea bags + treats."""
    return tea_count * 0.5 + treat_count * 0.75
    # tea_count and treat_count connected to tea_bags and treats in main, so it is all good when it reaches here
    # result will be a float


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    # shows text asking # of guests
    # nothing is called and nothing happens until inputting # of guests
    # main function is called at the END of code
