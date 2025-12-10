"""
author: UG_BEAST
"""


def read_input():
    with open("input.txt") as f:
        return f.read().strip()


def parse_lines(data):
    parsed_data = []
    for line in data.splitlines():
        if not line:
            continue

        parsed_data.append(line)
    return parsed_data


def part1(data):
    result = 0
    coords = []
    for line in data:
        a, b = line.split(",")
        coords.append((int(a), int(b)))
    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            result = max((abs(x2 - x1) + 1) * (abs(y2 - y1) + 1), result)
    return result


def part2(data):
    result = 0

    coords = []
    for line in data:
        a, b = line.split(",")
        coords.append((int(a), int(b)))

    return result


def main():
    raw_input = read_input()
    data = parse_lines(raw_input)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
