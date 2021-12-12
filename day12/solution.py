# Day 12: Passage Pathing
# https://adventofcode.com/2021/day/12

from collections import Counter

FILENAME = "input.txt"

adjacencies = {}

with open(FILENAME) as f:
    for line in f:
        a, b = line.rstrip("\n").split("-")

        adjacencies[a] = adjacencies.get(a, set()) | set([b])
        adjacencies[b] = adjacencies.get(b, set()) | set([a])


########################
#        Part 1        #
########################


def count_paths_p1(adjacencies, path=["start"]):
    if path[-1] == "end":
        return 1

    paths = 0
    for adj in adjacencies[path[-1]]:
        if adj != "start" and (not adj.islower() or adj not in path):
            paths += count_paths_p1(adjacencies, path + [adj])

    return paths


paths = count_paths_p1(adjacencies)
print("Solution to part 1:", paths)  # 5076


########################
#        Part 2        #
########################


def count_paths_p2(adjacencies, path=["start"]):
    if path[-1] == "end":
        return 1

    paths = 0
    for adj in adjacencies[path[-1]]:
        if adj != "start":
            if adj.islower():
                if (
                    adj not in path
                    or max(Counter(s for s in path if s.islower()).values()) == 1
                ):
                    paths += count_paths_p2(adjacencies, path + [adj])
            else:
                paths += count_paths_p2(adjacencies, path + [adj])

    return paths


paths = count_paths_p2(adjacencies)
print("Solution to part 2:", paths)  # 145643
