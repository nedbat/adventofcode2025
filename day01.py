with open("day01_input.txt") as f:
    nums = []
    for line in f:
        nums.append(int(line[1:]))
        if line[0] == "L":
            nums[-1] *= -1

pos = 50
zeros = 0
for num in nums:
    pos += num
    pos %= 100
    if pos == 0:
        zeros += 1

print(f"Part 1: There were {zeros} zeros")

# Part 2 the simplistic way.

pos = 50
zeros = 0
for num in nums:
    turn = -1 if num < 0 else 1
    for _ in range(abs(num)):
        pos += turn
        pos %= 100
        if pos == 0:
            zeros += 1

print(f"Part 2: there were {zeros} zeros")

# Part 2 a better way.

pos = 50
zeros = 0
for num in nums:
    pos0 = pos
    pos += num
    if pos > 0:
        zeros += pos // 100
    else:
        zeros += abs(pos // 100)
        if pos % 100 == 0:
            zeros += 1
        if pos0 == 0:
            zeros -= 1
    pos %= 100

print(f"Part 2: there were {zeros} zeros")
