# Day 6: Lanternfish
# https://adventofcode.com/2021/day/6

from collections import Counter
import numpy as np
import numpy.linalg as LA

FILENAME = "input.txt"

population = np.zeros(9, dtype=int)

with open(FILENAME) as f:
    counter = Counter(int(fish) for fish in f.read().strip("\n").split(","))
    for k, v in counter.items():
        population[k] += v

# simulation matrix that defines the state transitions
sim_matrix = np.array(
    [
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0],  # <- generate new lanternfish
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)


########################
#        Part 1        #
########################

# 345793
print("Solution to part 1:", np.sum(LA.matrix_power(sim_matrix, 80) @ population))


########################
#        Part 2        #
########################

# 1572643095893
print("Solution to part 2:", np.sum(LA.matrix_power(sim_matrix, 256) @ population))
