"""
author: UG_BEAST
Similar to rotating dial problem in codeforces !!
"""


def read_input():
    with open("input.txt") as f:
        return f.read().strip()


def parse_lines(data):
    i = []  # instructions list divided into direction and amount to move.
    for line in data.splitlines():
        if not line:
            continue
        d = line[0]
        amt = int(line[1:])
        i.append((d, amt))
    return i


def part1(data):
    i = parse_lines(data)
    c_pos = 50
    hits = 0  # no. of times the dial hits 0.

    for d, amt in i:
        if d == "R":
            c_pos = (c_pos + amt) % 100
        elif d == "L":
            c_pos = (c_pos - amt) % 100

        if c_pos == 0:
            hits += 1

    return hits


def part2(data):
    i = parse_lines(data)
    c_pos = 50
    hits = 0

    for d, amt in i:
        if d == "R":
            hits = (c_pos + amt) // 100 - (
                c_pos // 100
            )  # total hits = end hits - start hits
            hits += hits

            c_pos = (c_pos + amt) % 100

        elif d == "L":
            hits = (c_pos - 1) // 100 - (c_pos - amt - 1) // 100
            hits += hits
            c_pos = (c_pos - amt) % 100

    return hits


def main():
    data = read_input()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
