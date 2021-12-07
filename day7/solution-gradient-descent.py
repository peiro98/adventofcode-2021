# Day 7: The Treachery of Whales
# https://adventofcode.com/2021/day/7

import numpy as np


FILENAME = "input.txt"

with open(FILENAME) as f:
    positions = np.array([int(x) for x in f.read().strip("\n").split(",")])


########################
#        Part 1        #
########################

# start from a random position
x = np.random.randint(positions.min(), positions.max())
for i in range(100):
    # compute the derivative of the total fuel consumption wrt the current target
    derivative = -np.sum(np.sign(positions - x))
    lr = 0.1 ** (1 + (i // 100))
    # update the value of the target
    x = x - lr * derivative
    # recompute the fuel consumption
    fuel = np.abs(positions - round(x)).sum()

assert fuel == 345197
print("Solution to part 1:", fuel)


########################
#        Part 2        #
########################

# start from a random position
x = np.random.randint(positions.min(), positions.max())
for i in range(200):
    # compute the derivative of the total fuel consumption wrt the current target
    derivative = -np.sum(((2 * np.abs(positions - x) + 1) * np.sign(positions - x)) / 2)
    lr = 0.001 ** (1 + (i // 100))
    # update the value of the target
    x = round(x - lr * derivative)
    # recompute the fuel consumption
    fuel = np.abs(positions - x)
    fuel = ((fuel ** 2 + fuel) // 2).sum()

assert fuel == 96361606
print("Solution to part 2:", fuel)
