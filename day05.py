import dataclasses

import pytest

TEST_INPUT = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

REAL_INPUT = open("day05_input.txt").read()


@dataclasses.dataclass
class Db:
    fresh_ranges: list[tuple[int, int]]
    available: list[int]

    @classmethod
    def parse(cls, text: str):
        db = cls([], [])
        for line in text.splitlines():
            if "-" in line:
                pair = tuple(map(int, line.split("-")))
                assert pair[0] <= pair[1]
                db.fresh_ranges.append(pair)
            elif line:
                db.available.append(int(line))
        return db

    def fresh_ingredients(self):
        ranges = [range(a, b + 1) for a, b in self.fresh_ranges]
        for ingredient in self.available:
            if any(ingredient in r for r in ranges):
                yield ingredient


def test_parse():
    db = Db.parse(TEST_INPUT)
    assert db.fresh_ranges == [(3, 5), (10, 14), (16, 20), (12, 18)]
    assert db.available == [1, 5, 8, 11, 17, 32]


def part1(text):
    db = Db.parse(text)
    return sum(1 for ing in db.fresh_ingredients())


def test_part1():
    assert part1(TEST_INPUT) == 3


print(f"Part 1: there are {part1(REAL_INPUT)} fresh ingredients")


# Part 2: it doesn't work, and I'm not enjoying debugging it. Done.

def overlap(r1, r2):
    # https://nedbatchelder.com/blog/201310/range_overlap_in_two_compares.html
    return r1[1] >= r2[0] and r2[1] >= r1[0]


def union(r1, r2):
    assert r1[0] <= r1[1]
    assert r2[0] <= r2[1]
    return (min(r1[0], r2[0]), max(r2[1], r2[1]))


def add_one_range(r1s, r2):
    added = set()
    for r1 in r1s:
        if overlap(r1, r2):
            r2 = union(r1, r2)
        else:
            added.add(r1)
    added.add(r2)
    return sorted(added)

def part2(text):
    db = Db.parse(text)
    ranges = [(a, b) for a, b in db.fresh_ranges]
    combined = set()
    for r in sorted(ranges):
        combined = add_one_range(combined, r)
    total = sum(b - a + 1 for a, b in combined)
    return total


def test_part2():
    assert part2(TEST_INPUT) == 14

print(f"Part 2: there are {part2(REAL_INPUT)} fresh ingredients")
