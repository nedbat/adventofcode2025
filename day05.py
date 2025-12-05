import dataclasses

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
                db.fresh_ranges.append(tuple(map(int, line.split("-"))))
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
