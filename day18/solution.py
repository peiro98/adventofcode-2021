# Day 18: Snailfish
# https://adventofcode.com/2021/day/18
# 
# NOTE: definitely not the best possible solution

from typing import Generator
from functools import reduce
from itertools import combinations, chain

FILENAME = "input.txt"


def parse(line: Generator[str, None, None]):
    """Parse a snailfish number from a string generator"""
    content = []
    for ch in line:
        if ch == "]":
            break
        elif ch.isdigit():
            content.append(int(ch))
        elif ch == "[":
            content.append(parse(line))
        # everything else (comma, spaces, etc...) => skip
    return content


def parse_from_string(line: str):
    """Parse a snailfish number from a string"""
    return parse(x for x in line)


def explode(expr, depth=0, rmax=0, found=False):
    if (
        not found
        and depth >= 4
        and isinstance(expr, list)
        and all(isinstance(v, int) for v in expr)
    ):
        # replace the snailfish number with 0 and backpropagate the two regular numbers
        return 0, expr, True

    content = []
    lmax = 0
    for value in expr:
        if isinstance(value, int):
            content.append(value + rmax)
            rmax = 0
        else:
            # value to insert, numbers to backpropagate and a
            # boolean that identifies if this branch leads to the exploded value
            value, (_lmax, rmax), path_to_found = explode(value, depth + 1, rmax, found)

            if not found and path_to_found:
                # the traversed branch leads to the exploded value
                # => propagate the left value
                if len(content) and _lmax:
                    numbers = content

                    while type(numbers[-1]) == list:
                        numbers = numbers[-1]

                    numbers[-1] += _lmax
                else:
                    # the value can not be propagated (no values on the left)
                    # leave the job to the parent caller
                    lmax = _lmax
                found = True

            content.append(value)

    return content, (lmax, rmax), found


def split(v, done=False):
    if type(v) == int:
        if v >= 10:
            return [v // 2, (v + 1) // 2], True
        return v, False

    values = []
    for vv in v:
        if not done:
            vv, _done = split(vv, done)
            done = done or _done
        values.append(vv)

    return values, done


def add(a, b):
    res = [a, b]

    keep_going = True
    while keep_going:
        while keep_going:
            res, _, keep_going = explode(res)
        res, keep_going = split(res)
    return res


with open(FILENAME) as f:
    operands = [parse_from_string(line.rstrip("\n"))[0] for line in f.readlines()]


def compute_magnitude(v):
    return (
        v
        if type(v) == int
        else 3 * compute_magnitude(v[0]) + 2 * compute_magnitude(v[1])
    )


print("Solution to part 1:", compute_magnitude(reduce(add, operands)))  # 3359

max_magnitude = max(
    compute_magnitude(add(op1, op2))
    for op1, op2 in chain(combinations(operands, 2), combinations(operands[::-1], 2))
)

print("Solution to part 2:", max_magnitude)  # 4616
