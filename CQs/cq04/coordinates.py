"""get_coords defined"""

__author__: str = "730763577"


def get_coords(xs: str, ys: str) -> None:
    """Funct prints formatted pairs of each char in 2 input strings"""
    xindex: int = 0
    # index variable for xs
    xchar: str = ""
    # specific character currently accessed in xs by xindex
    ychar: str = ""
    # specific character currently accessed in ys by yindex

    while xindex < len(xs):
        # xindex must be 1 less than length of xs to prevent IndexError
        xchar = xs[xindex]
        # xindex accesses xs, set as local variable xchar
        yindex: int = 0
        # index variable for ys
        # note it's location is not the same as xindex!!!!
        # yindex's location must by INSIDE while loop so yindex is reset after inner while loops finishes running
        while yindex < len(ys):
            # yindex must be 1 less than length of ys to prevent IndexError
            ychar = ys[yindex]
            # yindex accesses ys, set as local variable ychar
            print(f"({xchar}, {ychar})")
            # format prints as (x, y)
            yindex += 1
            # add 1 to yindex INSIDE the while loop to prevent infinite running
        xindex += 1
        # ^ same reasoning for xindex


# xs prints with all letters of ys
# before moving onto next letter of xs
