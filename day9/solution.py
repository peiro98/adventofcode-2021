# Day 9: Smoke Basin
# https://adventofcode.com/2021/day/9

import numpy as np
import itertools
from collections import deque

FILENAME = "input.txt"

# top, right, bottom, left
SORROUNDINGS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

map = np.genfromtxt(FILENAME, delimiter=1, dtype=int)
map = np.pad(map, 1, constant_values=9)


########################
#        Part 1        #
########################

basins = np.zeros(map.shape, dtype=int)
for y, x in itertools.product(range(1, map.shape[0] - 1), range(1, map.shape[1] - 1)):
    if all(map[y + dy, x + dx] > map[y, x] for dy, dx in SORROUNDINGS):
        basins[y, x] = 1  # (y, x) is a basin

print("Solution to part 1:", np.sum(basins * (1 + map)))


########################
#        Part 2        #
########################

# assign a number to each basin
identifiers = np.arange(1, np.sum(basins > 0) + 1)
basins[basins > 0] = identifiers

for basin in identifiers:
    if not np.any(basins == basin):
        continue

    points = deque()
    points.append(np.argwhere(basins == basin)[0])

    while points:
        y, x = points.pop()

        # the sorrounding points must be either gte the current point
        # or belong to the same island
        neighbours = [(y + dy, x + dx) for dy, dx in SORROUNDINGS]
        if all(
            map[_y, _x] >= map[y, x] or basins[_y, _x] == basin for _y, _x in neighbours
        ):
            # assign the points to the island
            basins[y, x] = basin

            # and evaluate all the neighbours
            for py, px in neighbours:
                if basins[py, px] == 0 and map[py, px] < 9:
                    points.append((py, px))

# find the top three largest basins
a, b, c = sorted(np.sum(basins == i) for i in identifiers)[-3:]
print("Solution to part 2:", a * b * c)  # 1391940
