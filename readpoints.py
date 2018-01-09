#!/usr/bin/python3
# Copyright (c) 2018 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.


# Read points of a "Robot Tour" problem (Skiena, Algorithm Design
# Manual [2nd ed], Chapter 1) from a file.

def read_points(f):
    "Read tour points from f."

    coords = []
    for line in f:
        x, y = line.split()
        x = float(x)
        y = float(y)
        coords.append((x, y))
    return coords
