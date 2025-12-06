import functools
import operator

TEST_INPUT = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

REAL_INPUT = open("day06_input.txt").read()

def parse(text):
    nums = []
    for line in text.splitlines():
        if "*" in line:
            ops = line.split()
        else:
            nums.append([int(n) for n in line.split()])
    return list(zip(*nums)), ops

def test_parse():
    assert parse(TEST_INPUT) == (
        [
            (123, 45, 6),
            (328, 64, 98),
            (51, 387, 215),
            (64,  23, 314),
        ],
        ["*", "+", "*", "+"]
    )

def part1(text):
    numss, ops = parse(text)
    total = 0
    for nums, op in zip(numss, ops):
        if op == "+":
            start, op = 0, operator.__add__
        else:
            start, op = 1, operator.__mul__
        ans = functools.reduce(op, nums, start)
        total += ans
    return total

def test_part1():
    assert part1(TEST_INPUT) == 4277556

print(f"Part 1: {part1(REAL_INPUT)}")
