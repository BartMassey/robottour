#!/usr/bin/python3
# Copyright (c) 2018 Bart Massey

# Graphically display solutions to a "Robot Tour" problem
# (Skiena, Algorithm Design Manual [2nd ed], Chapter 1).

from turtle import *
from sys import argv, stdin
from dist import tour_length

from readpoints import read_points

def draw_tour(coords):
    "Draw the tour given by (augmented) coords."

    penup()
    for c in coords:
        goto(*c)
        dot(5 * pensize(), "black")
        pendown()


# Tour colors to be used, in order.
colors = ["red", "blue", "purple", "orange"]

def process_tour(fd, n):
    "Read tour n from fd and draw it."

    # Get the tour and loop it back to start.
    ps = read_points(fd)
    ps.append(ps[0])
    
    # Draw the length and the tour.
    pencolor(colors[n])
    penup()
    goto(0, 0.8 - 0.2 * n)
    pendown()
    write(tour_length(ps))
    draw_tour(ps)

# Do the processing.
if __name__ == "__main__":
    # Set up the display.
    screensize(1000, 1000)
    setworldcoordinates(0, 0, 1, 1)

    # Read from stdin if no arguments, else treat each
    # argument as a tour filename.
    if len(argv) < 2:
        process_tour(stdin, "black")
    else:
        n = 0
        for fname in argv[1:]:
            f = open(fname, "r")
            process_tour(f, n)
            n += 1
    done()
