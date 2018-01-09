#!/usr/bin/python3
# Copyright (c) 2018 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.


# Generate a "Robot Tour" problem (Skiena, Algorithm Design
# Manual [2nd ed], Chapter 1).

from random import random
from math import sqrt
from sys import argv

def coord(n):
    """Generate a random coordinate in the range 0..1
    distributed according to sqrt."""

    return round(sqrt(random()), 3)

def points(n):
    """Generate a list of n random points with coords in the
    range 0..1"""

    result = []
    for _ in range(n):
        result.append((coord(n), coord(n)))
    return result

# Generate an instance.
if __name__ == "__main__":
    n = int(argv[1])
    ps = points(n)
    for p in ps:
        print(*p)
