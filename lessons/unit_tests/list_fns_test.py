"""Doing stuff w python libraries! (I think)"""

from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    """Test that get first returns first elem"""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert get_first(fruits) == "apples"

def test_remove_first_ret_value() -> None:
    """Test that remove first returns None"""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert remove_first(fruits) == None

def test_remove_first_behavior() -> None:
    """Test that remove first removes first element"""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    remove_first(fruits)
    assert fruits == ["oranges", "bananas"]

def test_get_first_edge