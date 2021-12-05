# Day 5: Hydrothermal Venture
# https://adventofcode.com/2021/day/5

import re
from collections import Counter

FILENAME = "input.txt"

lines = []

with open(FILENAME) as f:
    for line in f:
        m = re.match(r"(\d+),(\d+) -> (\d+),(\d+).*", line)
        x1, y1, x2, y2 = map(int, m.groups())
        lines.append(((x1, y1), (x2, y2)))

########################
#        Part 1        #
########################

# expand lines into points
points = [
    (x1, min(y1, y2) + i)
    for (x1, y1), (x2, y2) in lines
    if x1 == x2
    for i in range(abs(y1 - y2) + 1)
]
points += [
    (min(x1, x2) + i, y1)
    for (x1, y1), (x2, y2) in lines
    if y1 == y2
    for i in range(abs(x1 - x2) + 1)
]

print("Solution to part 1:", sum(v > 1 for v in Counter(points).values()))  # 4745

########################
#        Part 2        #
########################

# expand lines into points
points += [
    (x1 + i * (1 if x1 < x2 else -1), y1 + i * (1 if y1 < y2 else -1))
    for (x1, y1), (x2, y2) in lines
    if x1 != x2 and y1 != y2
    for i in range(abs(y1 - y2) + 1)
]

print("Solution to part 2:", sum(v > 1 for v in Counter(points).values()))  # 18442
