# Robot Tour
Copyright (c) 2018 Bart Massey

This Python 3 code deals with the "Robot Tour" (actually
Traveling Salesworker) problem as described in Skiena,
*Algorithm Design Manual* [2nd ed], Chapter 1.

In addition to some library code, there are four basic
programs.

* `tourinst.py` generates random point clouds on `stdout`.

* `besttour.py` does exhaustive search of all possible
   permutations to find an optimal tour of the point cloud
   given on `stdin`, writing the solution to `stdout`.

* `nntour.py` does a modified greedy nearest-neighbor tour
   that works from both ends to find a reasonable tour of
   the point cloud given on `stdin`, writing the solution to
   `stdout`.

* `pairtour.py` connects nearest available neighbors
   piecewise to find a reasonable tour of the point cloud
   given on `stdin`, writing the solution to `stdout`.

* `showtour.py` uses Turtle Graphics to display one or more
  tours and their lengths. If no arguments are given, it
  will read the tour from `stdin`. Otherwise it treats each
  argument as the filename of a tour.

The `tours` directory contains some outputs.

This program is licensed under the "MIT License".  Please
see the file LICENSE in the source distribution of this
software for license terms.
