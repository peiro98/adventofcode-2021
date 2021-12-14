# Day 14: Extended Polymerization
# https://adventofcode.com/2021/day/14

from collections import Counter

FILENAME = "input.txt"

with open(FILENAME) as f:
    lines = f.readlines()
    template = lines[0].rstrip("\n")

    rules = dict()
    for line in lines[2:]:
        lhs, rhs = line.rstrip("\n").split("->")
        rules[lhs.strip()] = rhs.strip()


def evolve(template, rules, steps):
    state = Counter(a + b for a, b in zip(template, template[1:]))

    for _ in range(steps):
        new_state = Counter()

        for pair in state.keys():
            if pair in rules:
                # lhs and rhs of the rule
                lhs, rhs = pair, rules[pair]
                new_state.update({lhs[0] + rhs: state[lhs], rhs + lhs[1]: state[lhs]})
            else:
                new_state.update({pair: state[pair]})

        state = new_state

    frequencies = Counter(template[-1])
    for k, v in state.items():
        frequencies.update({k[0]: +v})

    return max(frequencies.values()) - min(frequencies.values())


########################
#        Part 1        #
########################

print("Solution to part 1:", evolve(template, rules, 10))  # 2915


########################
#        Part 2        #
########################

print("Solution to part 2:", evolve(template, rules, 40))  # 3353146900153
