from turtle import *
from sys import argv, stdin
from dist import tour_length

from readpoints import read_points

def draw_tour(coords):
    penup()
    for c in coords:
        goto(*c)
        dot(5 * pensize(), "black")
        pendown()


colors = ["red", "blue", "purple", "orange"]

def process_tour(fd, n):
    ps = read_points(fd)
    ps.append(ps[0])
    
    pencolor(colors[n])
    penup()
    goto(0, 0.8 - 0.2 * n)
    pendown()
    write(tour_length(ps))
    draw_tour(ps)

if __name__ == "__main__":
    screensize(1000, 1000)
    setworldcoordinates(0, 0, 1, 1)
    if len(argv) < 2:
        process_tour(stdin, "black")
    else:
        n = 0
        for fname in argv[1:]:
            f = open(fname, "r")
            process_tour(f, n)
            n += 1
    done()
