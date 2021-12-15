# Day 15: Chiton
# https://adventofcode.com/2021/day/15


import numpy as np
from heapq import heappush, heappop

FILENAME = "input.txt"

risks = np.genfromtxt(FILENAME, delimiter=1, dtype=np.int8)


def djkstra(grid, source, target):
    pq = [(0, source)]

    # tracking the preceding nodes is not required in this problem
    # prev = {v: None for v in distances.keys()}
    distances = {source: 0}

    while True:
        distance, (x, y) = heappop(pq)

        if (x, y) == target:
            return distance

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            tx, ty = x + dx, y + dy  # target of the new point

            if tx < 0 or ty < 0 or tx >= grid.shape[0] or ty >= grid.shape[1]:
                continue

            # compute the new distance for (x + dx, y + dy)
            new_distance = distance + grid[tx, ty]

            if new_distance < distances.get((tx, ty), np.inf):
                distances[(tx, ty)] = new_distance
                heappush(pq, (new_distance, (tx, ty)))
                # prev[(tx, ty)] = (x, y)


########################
#        Part 1        #
########################

print(djkstra(risks, (0, 0), (risks.shape[0] - 1, risks.shape[1] - 1)))  # 685


########################
#        Part 2        #
########################

risks_p2 = np.hstack([risks + i for i in range(5)])
risks_p2 = np.vstack([risks_p2 + i for i in range(5)])
risks_p2[risks_p2 > 9] = risks_p2[risks_p2 > 9] % 10 + 1

print(djkstra(risks_p2, (0, 0), (risks_p2.shape[0] - 1, risks_p2.shape[1] - 1)))  # 2995
