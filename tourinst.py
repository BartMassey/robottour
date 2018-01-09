#!/usr/bin/python3
# Copyright (c) 2018 Bart Massey

# Generate a "Robot Tour" problem (Skiena, Algorithm Design
# Manual [2nd ed], Chapter 1).

from random import random
from math import sqrt
from sys import argv

# Generate a random coordinate in the range 0..n.
def coord(n):
    return round(sqrt(random()), 3)

# Generate a list of n random points with coords in the range
# 0..n
def points(n):
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
