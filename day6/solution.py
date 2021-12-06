# Day 6: Lanternfish
# https://adventofcode.com/2021/day/6

from collections import Counter

NEWBORN_VALUE = 8
RESET_VALUE = 6

FILENAME = "input.txt"


with open(FILENAME) as f:
    population = [int(fish) for fish in f.read().strip("\n").split(",")]

# initial population state
stats = {i: 0 for i in range(NEWBORN_VALUE + 1)} | Counter(population)


def simulate(stats, n_iterations):
    for _ in range(n_iterations):
        new_stats = {
            i: stats[(i + 1) % (NEWBORN_VALUE + 1)] for i in range(NEWBORN_VALUE + 1)
        }

        # reset the fishes that just generated a new fish
        new_stats[RESET_VALUE] += stats[0]
        stats = new_stats

    return sum(stats.values())


########################
#        Part 1        #
########################

print("Solution to part 1:", simulate(stats, 80))  # 345793


########################
#        Part 2        #
########################

print("Solution to part 2:", simulate(stats, 256))  # 1572643095893
