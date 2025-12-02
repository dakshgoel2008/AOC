"""
author: UG_BEAST
"""


def read_input():
    with open("input.txt") as f:
        return f.read().strip()


def parse_lines(data):
    parsed_data = []
    for line in data.split(","):
        if not line:
            continue

        parsed_data.append(line)
    return parsed_data


def part1(data):
    ans = 0
    for j in data:
        l, r = map(int, j.split("-"))
        for num in range(l, r + 1):
            s = str(num)
            length = len(s)
            if length % 2 != 0:
                continue
            mid = length // 2
            first_half = s[:mid]
            second_half = s[mid:]
            if first_half == second_half:
                ans += num
    return ans


def periodic(s):
    length = len(s)
    # take a window size of i length and check if string can be made by repeating that window
    for i in range(1, length // 2 + 1):
        if length % i == 0:
            if s == s[:i] * (length // i):
                return True
    return False


def part2(data):
    ans = 0
    for j in data:
        l, r = map(int, j.split("-"))
        for num in range(l, r + 1):
            s = str(num)
            if periodic(s):
                ans += num
    return ans


def main():
    raw_input = read_input()
    data = parse_lines(raw_input)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
