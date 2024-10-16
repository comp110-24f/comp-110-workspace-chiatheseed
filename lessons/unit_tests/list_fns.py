"""Used for lessons Mon Oct 14"""


def get_first(input: list[str]) -> str:
    return input[0]


def remove_first(input: list[str]) -> None:
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    first: str = input[0]
    input.pop(0)
    return first
