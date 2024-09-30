"""Practicing with conditionals."""

__author__: str = "730763577"


def less_than_10(num: int) -> bool:
    """Tells us if num < 10"""
    if num < 10:
        return True
    else:
        return False


print(less_than_10(num=12))


def wake_up(alarm: bool) -> str:
    """Return a messaage based on alarm going of or not"""
    if alarm is True:
        return "Wake up!"
    else:
        return "It's okay, you can sleep more :))"


print(wake_up(alarm=True))


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="food", letter="f"))
