TEST_INPUT = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".splitlines()

REAL_INPUT = open("day04_input.txt").read().splitlines()

def read_positions(lines):
    positions = set()
    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == "@":
                positions.add((x, y))

    return positions

def neighbors(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            yield x+dx, y+dy

def count_accessible(lines):
    positions = read_positions(lines)
    accessible = 0
    for x, y in positions:
        num_neighbors = sum((nxy in positions) for nxy in neighbors(x, y))
        if num_neighbors < 4:
            accessible += 1
    return accessible

def test_count_accessible():
    assert count_accessible(TEST_INPUT) == 13

print(f"Part 1: {count_accessible(REAL_INPUT)} are accessible")
