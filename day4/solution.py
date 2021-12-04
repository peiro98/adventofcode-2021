# Day 4: Giant Squid
# https://adventofcode.com/2021/day/4

import numpy as np
import re
from itertools import dropwhile, product, takewhile
from typing import Generator, Iterable


FILENAME = "input.txt"


def read_spaced_matrices(
    f: Iterable[str], dtype=int
) -> Generator[np.ndarray, None, None]:
    """
    Read several matrices from a string iterable spaced by an empty line.
    """

    # skip trailing '\n' and multiple spaces
    lines = (re.sub(r"\s+|\n", " ", line).strip() for line in f)

    while True:
        matrix = [
            [int(n) for n in line.split(" ")]
            for line in takewhile(
                lambda line: len(line) > 0,  # take non empty lines
                dropwhile(lambda line: len(line) == 0, lines),  # skip empty lines
            )
        ]

        if len(matrix) == 0:
            break

        yield np.array(matrix, dtype=dtype)


with open(FILENAME) as f:
    # read the numbers
    numbers = [int(x) for x in f.readline().rstrip("\n").split(",")]

    # read the boards
    boards = list(read_spaced_matrices(f))


########################
#        Part 1        #
########################

masks = [np.ones(board.shape, dtype=int) for board in boards]  # 1 = unmarked cell

result = None
for number, (board, mask) in product(numbers, zip(boards, masks)):
    mask[board == number] = 0

    if np.any(np.sum(mask, axis=0) == 0) or np.any(np.sum(mask, axis=1) == 0):
        result = np.sum(mask * board) * number
        break

print(f"Solution to part 1: {result}")  # 35670


########################
#        Part 2        #
########################

masks = [np.ones(board.shape, dtype=int) for board in boards]  # 1 = unmarked cell
completed = [False] * len(boards)

result = None
for number, (i, (board, mask)) in product(numbers, enumerate(zip(boards, masks))):
    if not completed[i]:
        mask[board == number] = 0

        if np.any(np.sum(mask, axis=0) == 0) or np.any(np.sum(mask, axis=1) == 0):
            result = np.sum(mask * board) * number
            completed[i] = True

print(f"Solution to part 2: {result}")  # 22704
