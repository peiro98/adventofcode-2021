# Day 3: Binary Diagnostic
# https://adventofcode.com/2021/day/3

import numpy as np

FILENAME = "input.txt"

converter = lambda col: np.array(list(str(col)))
report = np.loadtxt(FILENAME, converters={0: converter}, dtype=int, encoding="ascii")


########################
#        Part 1        #
########################

# compute the most common bit for each columns
most_common_bits = (
    np.sum(report * 2 - 1, axis=0) > 0
)  # True if 1 is the most common bit in the column, False otherwise
uncommon_bits = ~most_common_bits

# transform the most common bit into a decimal number
gamma_rate = int("".join(str(x) for x in most_common_bits.astype(int)), base=2)
epsilon_rate = int("".join(str(x) for x in uncommon_bits.astype(int)), base=2)

print("Solution to part 1:")
print(gamma_rate * epsilon_rate)  # 2640986


########################
#        Part 2        #
########################


def find_rating(report, bit_selector, depth=0):
    if report.shape[0] == 1 or depth == report.shape[1]:
        return report[0]

    bit = bit_selector(report[:, depth])
    return find_rating(report[report[:, depth] == bit], bit_selector, depth + 1)


o2_rating = find_rating(report, lambda col: int(np.sum(col * 2 - 1) >= 0))
o2_rating = int("".join(map(str, o2_rating)), base=2)

co2_rating = find_rating(report, lambda col: int(np.sum(col * 2 - 1) < 0))
co2_rating = int("".join(map(str, co2_rating)), base=2)

print("Solution to part 2: ")
print(o2_rating * co2_rating)  # 6822109
