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


def split_ranges(r1, r2):
    if overlap(r1, r2):
        a = min(r1[0], r2[0])
        b = max(r1[0], r2[0])
        c = min(r1[1], r2[1])
        d = max(r1[1], r2[1])
        splits = set()
        return {(a, b), (b, c), (c, d)}
    else:
        return {r1, r2}


@pytest.mark.parametrize(
    "r1, r2, res",
    [
        ((10, 20), (30, 40), {(10, 20), (30, 40)}),
        ((10, 20), (15, 25), {(10, 15), (15, 20), (20, 25)}),
        ((15, 25), (10, 20), {(10, 15), (15, 20), (20, 25)}),
        ((10, 20), (10, 20), {(10, 10), (10, 20), (20, 20)}),
        ((10, 10), (10, 20), {(10, 10), (10, 20)}),
    ],
)
def test_split_ranges(r1, r2, res):
    assert split_ranges(r1, r2) == res


def union_ranges(rs):
    print(f"starting with {rs}")
    splits = {rs[0]}
    for r in rs:
        new_splits = set()
        for s in splits:
            new_splits.update(split_ranges(r, s))
        print(f"intermediate: {new_splits=}")
        splits = sorted((a, b) for a, b in new_splits if a != b)
        print(f"intermediate: {splits=}")
        if len(splits) > 1:
            new_splits = set()
            for r1, r2 in zip(splits, splits[1:]):
                new_splits.update(split_ranges(r1, r2))
            print(f"intermediate: {new_splits=}")
            splits = sorted((a, b) for a, b in new_splits if a != b)
        print(f"adding {r=}, {splits=}")
    return splits


def part2(text):
    db = Db.parse(text)
    ranges = [(a, b + 1) for a, b in db.fresh_ranges]
    union = union_ranges(ranges)
    print(f"done: {sorted(union)}")
    total = sum(b - a for a, b in union)
    return total


def test_part2():
    assert part2(TEST_INPUT) == 14
