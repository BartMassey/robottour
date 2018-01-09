#!/usr/bin/python3
# Copyright (c) 2018 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.


# Solve a "Robot Tour" problem (Skiena, Algorithm Design
# Manual [2nd ed], Chapter 1) by exhaustive search.

from sys import stdin

from readpoints import read_points
from dist import *

def all_arrangements(s):
    "Return all arrangements of a sequence s."

    if s == []:
        return [[]]
    result = []
    for i in range(len(s)):
        rest = all_arrangements(s[:i] + s[i+1:])
        for r in rest:
            result.append([s[i]] + r)
    return result

def min_tour(ps):
    "Return a minimum-length tour covering the given point sequence."

    min_len = None
    min_tour = None
    for c in all_arrangements(ps):
        tl = tour_length(c)
        if min_len == None or tl < min_len:
            min_len = tl
            min_tour = c
    return min_tour

# Find and display a minimum tour.
if __name__ == "__main__":
    ps = read_points(stdin)
    m = min_tour(ps)
    for p in m:
        print(*p)
