# Day 7: The Treachery of Whales
# https://adventofcode.com/2021/day/7

import numpy as np


FILENAME = "input.txt"

with open(FILENAME) as f:
    positions = np.array([int(x) for x in f.read().strip("\n").split(",")])


########################
#        Part 1        #
########################

min_fuel = np.inf
for target in range(np.min(positions), np.max(positions) + 1):
    fuel = np.abs(positions - target).sum()
    min_fuel = min(min_fuel, fuel)

print("Solution to part 1:", min_fuel)  # 345197


########################
#        Part 2        #
########################

min_fuel = np.inf
for target in range(np.min(positions), np.max(positions) + 1):
    fuel = np.abs(positions - target)
    fuel = (fuel / 2) * (1 + fuel)  # Gauss formula for consecutive integers sum
    min_fuel = min(min_fuel, int(fuel.sum()))

print("Solution to part 2:", min_fuel)  # 345197
