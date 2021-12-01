# Day 1: Sonar Sweep
# https://adventofcode.com/2021/day/1

# part 1
readings = [int(line) for line in open("input.txt")]

print("Solution for part 1: ")
print(sum(n < next for n, next in zip(readings, readings[1:])))

# part 2
sequences = [
    sum(readings[i:i+3]) for i in range(len(readings) - 2)
]

print("Solution for part 2: ")
print(sum(n < next for n, next in zip(sequences, sequences[1:])))
