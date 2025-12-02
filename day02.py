import pytest

TEST_INPUT = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

with open("day02_input.txt") as f:
    REAL_INPUT = f.read().strip()


def is_invalid(n):
    n_digits = len(str(n))
    if n_digits % 2 == 0:
        divisor = 10 ** (n_digits // 2) + 1
        return n % divisor == 0
    return False


@pytest.mark.parametrize(
    "n, invalid",
    [
        (55, True),
        (555, False),
        (57, False),
        (6464, True),
        (123123, True),
        (123123123, False),
    ],
)
def test_invalid(n, invalid):
    assert is_invalid(n) is invalid


def invalid_ids(range_text):
    for pair in range_text.split(","):
        a, b = pair.split("-")
        for n in range(int(a), int(b) + 1):
            if is_invalid(n):
                yield n


def test_invalid_ids():
    assert list(invalid_ids(TEST_INPUT)) == [
        11,
        22,
        99,
        1010,
        1188511885,
        222222,
        446446,
        38593859,
    ]


def part1(range_text):
    return sum(invalid_ids(range_text))


print(f"Part 1: {part1(REAL_INPUT)}")
