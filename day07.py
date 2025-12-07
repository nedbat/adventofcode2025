TEST_INPUT = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

REAL_INPUT = open("day07_input.txt").read()

import collections
from dataclasses import dataclass, field

@dataclass
class Manifold:
    start: int = 0
    rows: list[set[int]] = field(default_factory=list)
    beams: set[int] = field(default_factory=set)
    num_splits: int = 0

    @classmethod
    def parse(cls, text):
        lines = text.splitlines()
        man = cls()
        man.start = lines[0].find("S")
        man.rows = [
            set(i for i, c in enumerate(line) if c == "^")
            for line in lines[1:]
        ]
        return man

    def run(self):
        self.beams = {self.start}
        self.num_splits = 0
        for row in self.rows:
            hits = row & self.beams
            self.num_splits += len(hits)
            self.beams -= hits
            for hit in hits:
                self.beams.update({hit - 1, hit + 1})


def part1(text):
    man = Manifold.parse(text)
    man.run()
    return man.num_splits

def test_part1():
    assert part1(TEST_INPUT) == 21

print(f"Part 1: {part1(REAL_INPUT)} splits")

def many_timelines(man):
    num_paths = collections.defaultdict(int)
    num_paths[man.start] = 1
    for row in man.rows:
        for pos in row:
            n = num_paths[pos]
            num_paths[pos] = 0
            num_paths[pos-1] += n
            num_paths[pos+1] += n
    return sum(num_paths.values())

def part2(text):
    man = Manifold.parse(text)
    return many_timelines(man)

def test_part2():
    assert part2(TEST_INPUT) == 40

print(f"Part 2: {part2(REAL_INPUT)} timelines")
