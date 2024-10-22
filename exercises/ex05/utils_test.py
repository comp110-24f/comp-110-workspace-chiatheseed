"""defining unit tests for utils.py"""

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index

__author__ = "730763577"

# 3 unit test functions for each function!!
    # At least 1 edge case
    # At least 2 use cases: one that tests what the function should return and one that tests how it should mutate (or not mutate) its input.

# use case
def test_only_evens_ret_list() -> None:
    """Tests that only_evens returns list[int]"""
    input_list: list[int] = [4, 5, 6]
    assert only_evens(input_list) == [4, 6]

# use case
def test_only_evens_mutate() -> None:
    """Tests that only_evens does not mutate input_list"""
    input_list: list[int] = [4, 5, 6]
    only_evens(input_list)
    assert input_list == [4, 5, 6]


# edge case
def test_only_evens_edge() -> None:
    """Tests that only_evens returns empty list given no evens"""

# use case
def test_sub_ret_list() -> None:
    """Tests that subs returns a list[int]"""
    alist: list[int] = [1, 2, 3, 4]
    idxs=1
    idxe=3
    assert sub(alist, idxs, idxe) == [2, 3]

# use case 
def test_sub_no_mutate() -> None:
    """Tests that subs does not mutate input list (alist)"""
    alist=[1, 2, 3, 4]
    idxs=1
    idxe=3
    sub(alist, idxs, idxe)
    assert alist == [1, 2, 3, 4]

# edge case
def test_sub_edge() -> None:
    """Tests that subs will return proper list[int] given negative idxs"""
    alist=[1, 2, 3, 4]
    idxs=-3
    idxe=3
    sub(alist, idxs, idxe)
    assert alist == [1, 2, 3, 4]

# use case
def test_add_at_index_IndexError() -> None:
    """Tests that add_at_index raises IndexError for an invalid index."""
    with pytest.raises(IndexError):
        add_at_index(input_list=[1], add_elem=2, idx_add=-3) 
        # an IndexError is raised for the case when the add_at_index is given an idx_add
        # that is greater than the length of our input_list
        # if IndexError is raised, test passes

# use case
def test_add_at_index_ret_list() -> None:
    """Tests that add_at_index returns a list[int]"""
    input_list: list[int] = [10, 9, 8, 7, 5]
    add_elem: int = 6
    idx_add: int = 4
    assert type(add_at_index(input_list, add_elem, idx_add)) == [10, 9, 8, 7, 6, 5]
    
# use case
def test_add_at_index_mutate() -> None:
    """Tests that add_at_index mutates input_list by adding specific elem at given index"""
    input_list: list[int] = [10, 9, 8, 7, 5]
    add_elem: int = 6
    idx_add: int = 4
    add_at_index(input_list, add_elem, idx_add)
    assert input_list == [10, 9, 8, 7, 6, 5]

# edge case
def test_add_at_index() -> None: