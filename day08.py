import itertools

TEST_INPUT = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

REAL_INPUT = open("day08_input.txt").read()


def parse(text):
    return [tuple(map(int, l.split(","))) for l in text.splitlines()]

def dist(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2


def circuits(text, n_connections):
    pts = parse(text)
    # Map point to sets, circuits containing those points.
    circuits = {pt: {pt} for pt in pts}
    ds = sorted((dist(a, b), a, b) for a,b in itertools.combinations(pts, 2))
    for _, a, b in ds:
        a_circuit = circuits[a]
        b_circuit = circuits[b]
        # if a_circuit == b_circuit:
        #     continue
        combined = a_circuit | b_circuit
        for cpt in combined:
            circuits[cpt] = combined
        n_connections -= 1
        if n_connections == 0:
            break

    unique_circuits = set(map(tuple, circuits.values()))
    circuits_by_size = sorted(unique_circuits, key=len, reverse=True)
    big3 = circuits_by_size[:3]
    return len(big3[0]) * len(big3[1]) * len(big3[2])

def test_circuits():
    assert circuits(TEST_INPUT, 10) == 40

print("Part 1:", circuits(REAL_INPUT, 1000))
