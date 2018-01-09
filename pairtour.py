#!/usr/bin/python3
# Copyright (c) 2018 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source distribution of
# this software for license terms.


# Solve a "Robot Tour" problem (Skiena, Algorithm Design
# Manual [2nd ed], Chapter 1) by greedy closest pair
# connection.

from sys import stdin

from readpoints import read_points
from dist import dist

def rep(partitions, i):
    for pi in range(len(partitions)):
        if i in partitions[pi]:
            return pi
    assert False

def join(partitions, i, j):
    pi = rep(partitions, i)
    pj = rep(partitions, j)
    partitions[pi] = partitions[pi] | partitions[pj]
    del partitions[pj]

def nearest_neighbors(ps, partitions, counts):
    """Return the indexes of the closest pair of points in ps
    such that endpoints are in different components and counts are right."""

    min_dist = None
    min_indices = None
    for i in range(len(ps)):
        if counts[i] >= 2:
            continue
        for j in range(len(ps)):
            if counts[j] >= 2:
                continue
            if rep(partitions, i) == rep(partitions, j):
                continue
            d = dist(ps[i], ps[j])
            if min_dist == None or d < min_dist:
                min_dist = d
                min_indices = (i, j)
    return min_indices

def pair_tour(ps):
    "Find a closest_pair tour of ps."

    partitions = [{i} for i in range(len(ps))]
    counts = [0] * len(ps)
    conns = []
    while len(conns) < len(ps) - 1:
        i, j = nearest_neighbors(ps, partitions, counts)
        conns.append((i, j))
        counts[i] += 1
        counts[j] += 1
        join(partitions, i, j)
    last = []
    for i in range(len(counts)):
        if counts[i] < 2:
            last.append(i)
    assert len(last) == 2
    conns.append(tuple(last))

    conn_points = []
    cur = 0
    while True:
        for i in range(len(conns)):
            found = False
            if conns[i][1] == cur:
                snd, fst = conns[i]
                conns[i] = (fst, snd)
            if conns[i][0] == cur:
                cur = conns[i][1]
                conn_points.append(ps[cur])
                del conns[i]
                found = True
                break
        assert found
        if cur == 0:
            return conn_points

# Find and display a closest-pair tour.
if __name__ == "__main__":
    ps = read_points(stdin)
    m = pair_tour(ps)
    for p in m:
        print(*p)
