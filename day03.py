TEST_INPUT = """\
987654321111111
811111111111119
234234234234278
818181911112111
""".splitlines()

REAL_INPUT = open("day03_input.txt").read().splitlines()

def max_joltage(bank):
    tens = max(bank[:-1])
    ones = max(bank[bank.find(tens)+1:])
    return int(tens) * 10 + int(ones)

def test_max_joltage():
    assert [max_joltage(b) for b in TEST_INPUT] == [98, 89, 78, 92]

def part1(bank):
    return sum(map(max_joltage, bank))

def test_part1():
    assert part1(TEST_INPUT) == 357

print(f"Part 1: max joltage = {part1(REAL_INPUT)}")
