# Day 2: 
# 

FILENAME = "input.txt"

# part 1
x, y = 0, 0

with open(FILENAME) as f:
    for line in f:
        command, value = line.rstrip("\n").split(" ")
        value = int(value)

        if command == "forward":
            x += value
        elif command == "down":
            y += value
        elif command == "up":
            y -= value

print("Solution to part 1: ")
print(x*y)

# part 2
x, y, aim = 0, 0, 0

with open(FILENAME) as f:
    for line in f:
        command, value = line.rstrip("\n").split(" ")
        value = int(value)

        if command == "forward":
            x += value
            y += value * aim
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value

print("Solution to part 2: ")
print(x*y)
