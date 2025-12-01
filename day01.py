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

print(f"There were {zeros} zeros")
