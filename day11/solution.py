# Day 11: Dumbo Octopus
# https://adventofcode.com/2021/day/1

import numpy as np
from itertools import product


FILENAME = "input.txt"

octopuses = np.genfromtxt(FILENAME, delimiter=1, dtype=int)


########################
#        Part 1        #
########################


def step(octopuses):
    # keep track of the octopuses that flashed during this step
    flashed = np.zeros(octopuses.shape, dtype=int)

    # queue points that have to be incremented
    queue = list((y, x) for y, x in product(range(10), repeat=2))

    while queue:
        y, x = queue.pop()

        # increment only octopuses that did not flash yet
        octopuses[y, x] += not flashed[y, x]

        if octopuses[y, x] <= 9:
            continue

        flashed[y, x] = 1
        octopuses[y, x] = 0

        # add all the sorrounding points to the list of flashing octpuses
        queue += [
            (y + dy, x + dx)
            for dy, dx in product([-1, 0, 1], repeat=2)
            if y + dy in range(10) and x + dx in range(10)
        ]

    return octopuses, flashed.sum()


n_flashes = 0
p1_octopuses = np.copy(octopuses)
for _ in range(100):
    p1_octopuses, n = step(p1_octopuses)
    n_flashes += n

print("Solution to part 1:", n_flashes)  # 1683


########################
#        Part 2        #
########################

n_steps = 0
n = 0
while n != 100:
    octopuses, n = step(octopuses)
    n_steps += 1

print("Solution to part 2:", n_steps)  # 788
