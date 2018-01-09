def read_points(f):
    coords = []
    for line in f:
        x, y = line.split()
        x = float(x)
        y = float(y)
        coords.append((x, y))
    return coords
