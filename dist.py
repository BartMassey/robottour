#!/usr/bin/python3
# Copyright (c) 2018 Bart Massey

# Compute point distances for a "Robot Tour" problem
# (Skiena, Algorithm Design Manual [2nd ed], Chapter 1).

from math import sqrt

def dist(p1, p2):
    "Compute the Euclidean distance between the given pair of points."

    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def tour_length(ps):
    "Compute the length of the point sequence ps considered as a tour."

    n = len(ps)
    l = 0
    for i in range(n):
        l += dist(ps[i], ps[(i + 1) % n])
    return l
