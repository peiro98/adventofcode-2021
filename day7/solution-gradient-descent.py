# Day 7: The Treachery of Whales
# https://adventofcode.com/2021/day/7

import numpy as np
from numpy.random.mtrand import triangular


FILENAME = "input.txt"

with open(FILENAME) as f:
    positions = np.array([int(x) for x in f.read().strip("\n").split(",")])


def find_min(func, derivative, x=0, lr=1, max_step=100):
    """Find the minimum of the provided function"""
    best_estimate, last_best_index = np.inf, 0

    for i in range(max_step):
        # update the value of the target
        x = x - lr * derivative(x)

        # recompute the minimum estimate
        new_estimate = func(x)

        if new_estimate < best_estimate:
            last_best_index = i
        else:
            lr = lr * 0.1  # the estimate is not improving => update the lr

        if i - last_best_index == 10 and not np.isinf(best_estimate):
            break

        best_estimate = min(best_estimate, new_estimate)

    return func(round(x))


########################
#        Part 1        #
########################

fuel = find_min(
    lambda x: np.abs(positions - x).sum(), lambda x: -np.sum(np.sign(positions - x))
)
print("Solution to part 1:", fuel)


########################
#        Part 2        #
########################

traingular = lambda x: (x ** 2 + x) / 2
fuel = find_min(
    lambda x: traingular(np.abs(positions - x)).sum(),
    lambda x: -np.sum(((2 * np.abs(positions - x) + 1) * np.sign(positions - x)) / 2),
    lr=0.001,
)
print("Solution to part 2:", fuel)


# NOTE: sum_i [sign(positions-x)] is zero when half the points
# lie above x and the other half below ==> x is the median of the values
