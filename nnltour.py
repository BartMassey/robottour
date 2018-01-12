#!/usr/bin/python3
# Copyright (c) 2018 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source distribution of
# this software for license terms.


# Solve a "Robot Tour" problem (Skiena, Algorithm Design
# Manual [2nd ed], Chapter 1) by limited-lookahead
# nearest-neighbor.

from sys import stdin, argv

from readpoints import read_points
from dist import *

def extend_path(path, ps, lookahead=0):
    """Add the closest point in ps to an end of path to that end
    of path and delete it from ps."""

    def update_path(end, cur_path, p):
        "Add p to the appropriate end of cur_path."
        if j == 0:
            cur_path.insert(0, ps[i])
        else:
            cur_path.append(ps[i])
        

    min_dist = None
    min_indices = None
    for i in range(len(ps)):
        for j in [0, -1]:
            d = None
            if lookahead > 0:
                tmp_path = list(path)
                update_path(j, tmp_path, ps[i])
                tmp_ps = list(ps)
                del tmp_ps[i]
                tour = nn_tour(tmp_path, tmp_ps, lookahead=lookahead-1)
                d = tour_length(tour)
            else:
                d = dist(ps[i], path[j])
            if min_dist == None or d < min_dist:
                min_dist = d
                min_indices = (i, j)
    i, j = min_indices
    update_path(j, path, ps[i])
    del ps[i]

def nn_tour(path, ps, lookahead=0):
    "Find a nearest-neighbor extension of path to tour of ps."

    while ps != []:
        extend_path(path, ps, lookahead=lookahead)
    return path

# Find and display a nearest-neighbor tour.
if __name__ == "__main__":
    lookahead = 0
    if len(argv) > 1:
        lookahead = int(argv[1])
    ps = read_points(stdin)
    path = [ps[0]]
    del ps[0]
    m = nn_tour(path, ps, lookahead=lookahead)
    for p in m:
        print(*p)
