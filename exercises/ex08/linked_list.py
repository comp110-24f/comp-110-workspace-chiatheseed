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

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str
        if self is None:
            return "None"
        else:
            rest = str(self.next)
            return f"{self.value} -> {rest}"


"""
three: Node = Node(30, None)
two: Node = Node(20, three)
one: Node = Node(10, two)
courses: Node = Node(110, Node(210, Node(301, None)))"""


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        # creates a variable that holds the str linked list up until the current node
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
    # in the "rest of the list"
    else:
        rest: int = last(head.next)
        print(f"Return recur: {head.value} -> {rest}")
        return rest


"""print(last(one))  # expect to print 2
print(last(courses))  # expect to print 301"""


def value_at(head: Node | None, index: int) -> int:
    """Returns the value of the Node stored at a given index."""
    # edge case - empty list
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # base case - index is 0
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Returns max value in the linked list."""
    # edge case - if the linked list is empty
    if head is None:
        raise ValueError("Cannot call max with None")
    # if there is only one node in the linked list
    if head.next is None:
        return head.value
    # if current node's value is greater, returns head.value
    # MISTAKE: comparing max(head.value) with max(head.next)
    # don't call max(head.value) since head.value is the current node evaluated in the current funct frame
    elif head.value > max(head.next):
        return head.value
    # otherwise, returns MAX(head.next)
    else:
        return max(head.next)


def linkify(list: list[int]) -> Node | None:
    """Returns a Linked List of Nodes with same values, in same order, as input list."""
    # base case - what the last 'step' is
    # the spliced list is empty
    if len(list) == 0:
        return None
    # recursive case - create nodes
    # smth must happen for recursive case to reach base case
    else:
        # putting linkify() in the node.next spot links previous node to the next node
        node = Node(list[0], linkify(list[1:]))
        # MISTAKE: not returning smth
        # not returning node leads to IndexError
        return node


# print(linkify([10, 20, 30]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a new linked list of nodes where each value in the input linked list is scaled by factor."""
    # base case - if list is empty; last step
    if head is None:
        return None
    # if there is just one node in the linked list
    else:
        node = Node(head.value * factor, scale(head.next, factor))
        return node


# print(scale(linkify([1, 2, 3]), 2))
