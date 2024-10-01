"""Imported function concat from concatenation.py"""

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords


__author__ = "730763577"


x: str = "123"
y: str = "abc"

print(concat(word1=x, word2=y))

print(get_coords(xs=x, ys=y))
