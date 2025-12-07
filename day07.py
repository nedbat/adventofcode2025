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
