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

def part1(banks):
    return sum(map(max_joltage, banks))

def test_part1():
    assert part1(TEST_INPUT) == 357

print(f"Part 1: max joltage = {part1(REAL_INPUT)}")

def max_joltage_n(bank, n):
    digits = []
    for i in range(n):
        # Grrr: it would be much more convenient if b[:-0] went to the end.
        end = -(n-1-i)
        digit = max(bank[:(end if end else None)])
        bank = bank[bank.find(digit)+1:]
        digits.append(digit)
    return int("".join(digits))

def test_max_joltage_n():
    assert [max_joltage_n(b, 12) for b in TEST_INPUT] == [987654321111, 811111111119, 434234234278, 888911112111]

def part2(banks):
    return sum(max_joltage_n(b, 12) for b in banks)

print(f"Part 2: max_joltage = {part2(REAL_INPUT)}")
