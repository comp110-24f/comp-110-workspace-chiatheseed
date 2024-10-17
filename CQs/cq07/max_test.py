"""Testing find max function"""

from CQs.cq07.find_max import find_and_remove_max

__author__: str = "730763577"


# One use case that ensures find_and_remove_max returns the expected value.
def test_find_and_remove_max_ret() -> None:
    """Tests that find_and_remove_max returns max value"""
    input_list: list[int] = [10, 4, 6, 10]
    assert find_and_remove_max(input_list) == 10


# One use case that ensures find_and_remove_max mutates the input in the expected way.
def test_find_and_remove_max_mut() -> None:
    """Tests that find_and_remove_max mutates list by removing all max values"""
    input_list: list[int] = [10, 4, 6, 10]
    find_and_remove_max(input_list)
    assert input_list == [4, 6]


# One edge case that ensures find_and_remove_max returns the correct value in case of an unconventional input."""
def test_find_and_remove_max_ret_empty() -> None:
    """Tests that find_and_remove_max returns -1 if input list is empty"""
    input_list: list[int] = []
    assert find_and_remove_max(input_list) == -1
