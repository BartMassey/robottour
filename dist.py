#!/usr/bin/python3
# Copyright (c) 2018 Bart Massey

from math import sqrt

# Compute the Euclidean distance between the given pair of points.
def dist(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Compute the length of the point sequence ps considered as a tour.
def tour_length(ps):
    n = len(ps)
    l = 0
    for i in range(n):
        l += dist(ps[i], ps[(i + 1) % n])
    return l
