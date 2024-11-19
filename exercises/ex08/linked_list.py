"""Copied linked_list module from lessons."""

from __future__ import annotations

__author__ = "730763577"


class Node:
    """Defining class Node."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializing attributes."""
        self.value = value
        self.next = next


three: Node = Node(30, None)
two: Node = Node(20, three)
one: Node = Node(10, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


"""print(to_str(one))
print(to_str(courses))"""


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base Case: when head is the last node
    # return its value!
    print(f"Enter last({head.value})")
    if head.next is None:
        print(f"Return base case: {head.value}")
        return head.value
    # Recursive Case:
    # figure out the last node (recursive call)
    # in the "rest of the list"
    # return this value!
    else:
        rest: int = last(head.next)
        print(f"Return recur: {head.value} -> {rest}")
        return rest


"""print(last(one))  # expect to print 2
print(last(courses))  # expect to print 301"""


def value_at(head: Node | None, index: int) -> int:
    """Returns the value of the Node stored at a given index or raises IndexError."""
    # edge case - empty list
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # base case - index is 0
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)

# VALUE AT
# inputs: head (Node | None) and index (int)

def max(head: Node)
    """Returns max value in the linked list."""
    