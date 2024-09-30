"""CL 11: Global Variables + Scope 
the first step: creating remove_chars function"""

__author__: str = "730763577"


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed"""
    copy: str = ""  # set up empty str to copy values over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
        index += 1
    return copy


remove_chars(msg="yoyo", char="o")
