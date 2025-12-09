import itertools

TEST_INPUT = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

REAL_INPUT = open("day09_input.txt").read()

def parse_pts(text):
    return set(tuple(map(int, l.split(","))) for l in text.splitlines())

def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def max_rect(pts):
    return max(area(p1, p2) for p1, p2 in itertools.combinations(pts, 2))    

def part1(text):
    return max_rect(parse_pts(text))

def test_part1():
    assert part1(TEST_INPUT) == 50

print(f"Part 1: largest rectangle is {part1(REAL_INPUT)}")
