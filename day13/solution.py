# Day 13: Transparent Origami
# https://adventofcode.com/2021/day/13
# NOTE: naive solution using numpy.flip (not optimized for large matrices)

import numpy as np
import matplotlib.pyplot as plt

FILENAME = "input.txt"

xx, yy = [], []
folds = []
with open(FILENAME) as f:
    for line in f:
        line = line.rstrip("\n")
        if "," in line:
            x, y = line.split(",")
            xx.append(int(x))
            yy.append(int(y))
        elif "=" in line:
            axis, offset = line.split("=")
            folds.append((axis[-1], int(offset)))

paper = np.zeros((max(xx) + 1, max(yy) + 1), dtype=bool)
paper[xx, yy] = True


############################
#        Part 1 & 2        #
############################

for i, (axis, offset) in enumerate(folds):
    if axis == "x":
        paper = paper[:offset] | np.flip(paper[offset + 1 :], axis=0)
    else:
        paper = paper[:, :offset] | np.flip(paper[:, offset + 1 :], axis=1)

    if i == 0:
        print("Solution to part 1:", np.sum(paper))  # 631


plt.imshow(paper.T)  # EFLFJGRF
plt.show()
