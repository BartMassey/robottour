#!/usr/bin/python3
# Copyright (c) 2018 Bart Massey

# Solve a "Robot Tour" problem (Skiena, Algorithm Design
# Manual [2nd ed], Chapter 1) by greedy nearest-neighbor
# (to either endpoint).

from sys import stdin

from readpoints import read_points
from dist import dist

def nearest_neighbors(ps):
    "Return the indexes of the closest pair of points in ps."

    min_dist = dist(ps[0], ps[1])
    min_indices = (0, 1)
    for i in range(len(ps)):
        for j in range(len(ps)):
            if i == j:
                continue
            d = dist(ps[i], ps[j])
            if d < min_dist:
                min_dist = d
                min_indices = (i, j)
    return min_indices

def extend_path(path, ps):
    """Add the closest point in ps to an end of path to that end
    of path and delete it from ps."""

    min_dist = None
    min_indices = None
    for i in range(len(ps)):
        for j in [0, -1]:
            d = dist(ps[i], path[j])
            if min_dist == None or d < min_dist:
                min_dist = d
                min_indices = (i, j)
    i, j = min_indices
    if j == 0:
        path.insert(0, ps[i])
    else:
        path.append(ps[i])
    del ps[i]

def nn_tour(ps):
    "Find a nearest-neighbor tour of ps."

    start, end = nearest_neighbors(ps)
    path = [ps[start], ps[end]]
    del ps[start]
    del ps[end - 1]
    while ps != []:
        extend_path(path, ps)
    return path

# Find and display a nearest-neighbor tour.
if __name__ == "__main__":
    ps = read_points(stdin)
    m = nn_tour(ps)
    for p in m:
        print(*p)
