# Day 10: Syntax Scoring
# https://adventofcode.com/2021/day/10

from functools import reduce

FILENAME = "input.txt"

openings = ["<", "(", "[", "{"]
closings = {"<": ">", "(": ")", "[": "]", "{": "}"}

# parser points
parser_points = {")": 3, "]": 57, "}": 1197, ">": 25137}

# autocomplete points
ac_points = {")": 1, "]": 2, "}": 3, ">": 4}


def parse(line):
    """Detect illegal characters and autocomplete sequences"""
    stack = []

    for symbol in line:
        if symbol in openings:
            stack.append(symbol)
        elif len(stack) > 0 and symbol == closings[stack[-1]]:
            # 'symbol' is the expected one
            stack = stack[:-1]
        else:
            # illegal character!
            return symbol, []

    # no illegal character found: return the expected closing characters
    return None, [closings[ch] for ch in stack[::-1]]


with open(FILENAME) as f:
    lines = [line.rstrip("\n") for line in f]


########################
#        Part 1        #
########################

total = sum(parser_points.get(parse(line)[0], 0) for line in lines)
print(f"Solution to part 1: {total}")  # 392421


########################
#        Part 2        #
########################

scores = []
for line in lines:
    illegal_ch, autocomplete = parse(line)

    if not illegal_ch:
        scores.append(
            reduce(lambda score, ch: (score * 5) + ac_points[ch], autocomplete, 0)
        )

middle_score = sorted(scores)[len(scores) // 2]
print("Solution to part 2:", middle_score)  # 2769449099
