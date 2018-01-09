#!/usr/bin/python3
# Copyright (c) 2018 Bart Massey

# Generate and solve a "Robot Tour" problem (Skiena, Algorithm Design
# Manual [2nd ed], Chapter 1) by exhaustive search.

from sys import stdin

from readpoints import read_points
from dist import *

# Return all arrangements of a sequence s.
def all_arrangements(s):
    if s == []:
        return [[]]
    result = []
    for i in range(len(s)):
        rest = all_arrangements(s[:i] + s[i+1:])
        for r in rest:
            result.append([s[i]] + r)
    return result

# Return a minimum-length tour covering the given point sequence.
def min_tour(ps):
    min_len = None
    min_tour = None
    for c in all_arrangements(ps):
        tl = tour_length(c)
        if min_len == None or tl < min_len:
            min_len = tl
            min_tour = c
    return min_tour

# Generate an instance and display a minimum tour.
if __name__ == "__main__":
    ps = read_points(stdin)
    m = min_tour(ps)
    for p in m:
        print(*p)