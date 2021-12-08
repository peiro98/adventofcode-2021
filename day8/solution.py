# Day 8: Seven Segment Search
# https://adventofcode.com/2021/day/8

from functools import reduce

FILENAME = "input.txt"

SEGMENTS = set("abcdefg")
DIGITS = [
    set("abcefg"), # 0
    set("cf"), # 1
    set("acdeg"), # 2
    set("acdfg"), # 3
    set("bcdf"), # 4
    set("abdfg"), # 5
    set("abdefg"), # 6
    set("acf"), # 7
    set("abcdefg"), # 8
    set("abcdfg"), # 9
]

patterns = []
outputs = []

with open(FILENAME) as f:
    for line in f:
        pattern, output = line.rstrip("\n").split("|")
        patterns.append([p.strip() for p in pattern.strip().split(" ")])
        outputs.append([o.strip() for o in output.strip().split(" ")])


########################
#        Part 1        #
########################

# count the easy digits (digits that can be represented with a unique number of segments)
n = sum(1 for output in outputs for digit in output if len(digit) in [2, 3, 4, 7])
print("Solution to part 1:", n)  # 493


########################
#        Part 2        #
########################

def decode(patterns, outputs):
    # initially, each segment is associated to any other segment
    rosetta = {segment: set(SEGMENTS) for segment in SEGMENTS}

    # patterns are represented with a varying number of segments in the range [2, 7]
    for num_segments in [2, 3, 5, 6]:
        # collect observed digits with a specific number of segments
        observed_digits = [set(p) for p in patterns if len(p) == num_segments]

        # collect "original" digits with a specific number of segments
        translated_digits = [d for d in DIGITS if len(d) == num_segments]

        # find the intersections between the segments of the observed patterns
        # find the intersections between the segments of the original digits
        # => use this information to reduce the number of possible values
        #    example: 2, 3 and 5 share the segments 'a', 'd' and 'g'
        for c in reduce(set.intersection, translated_digits):
            rosetta[c] &= reduce(set.intersection, observed_digits)

    # up to now, the rosetta dictionary may contain inconsistencies
    # => use the knowledge of the *certain* mappings to clean the dictionary
    while any(len(values) > 1 for values in rosetta.values()):
        for key in rosetta.keys():
            # remove from rosetta[key] all the certain mappings
            # example: rosetta['a'] = ('a', 'b', 'c'), rosetta['b'] = 'c'
            #          => 'c' can be safely removed from rosetta['a']
            rosetta[key] = rosetta[key].difference(
                *(v for k, v in rosetta.items() if len(v) == 1 and k != key)
            )

    # replace sets with values
    rosetta = {k: v.pop() for k, v in rosetta.items()}
    
    # translate the "original" segments using the computed mapping
    translated_digits = [set(rosetta[c] for c in digit) for digit in DIGITS]
    # use the translation to compute the output value
    output_value = [translated_digits.index(set(o)) for o in outputs]

    # convert the output value to a decimal number
    return sum(v * (10 ** idx) for idx, v in enumerate(reversed(output_value)))


n = sum(decode(pattern, output) for pattern, output in zip(patterns, outputs))
print("Solution to part 2:", n)
