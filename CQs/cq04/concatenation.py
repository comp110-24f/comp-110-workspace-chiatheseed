"""Concatenating global variables word1 and word 2 w/ concat function."""

__author__: str = "730763577"


def main() -> None:
    print(concat)


def concat(word1: str, word2: str) -> str:
    """Function returns the concatenation of the two input strings."""
    return word1 + word2


# global variables word1 and word 2
word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    # main is useful because concat function call will occur when I run concatentation.py
    # but not when I import it!"""
    print(concat(word1=word1, word2=word2))
