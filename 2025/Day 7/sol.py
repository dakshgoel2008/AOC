"""
author: UG_BEAST
"""

from collections import defaultdict


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
    ans = 0
    active_cols = set()
    rows = len(data)
    cols = len(data[0])

    # more generalised approach for finding the start row
    st_row = 0
    for r, line in enumerate(data):
        if "S" in line:
            # print(line.index("S"))
            st_row = r
            active_cols.add(line.index("S"))
            break

    for r in range(st_row, rows):
        next = set()
        for c in active_cols:
            ch = data[r][c]
            if ch == "^":
                ans += 1
                if c - 1 >= 0:
                    next.add(c - 1)
                if c + 1 < cols:
                    next.add(c + 1)
            else:
                next.add(c)
        active_cols = next
    return ans


def part2(data):
    # dp approach
    rows = len(data)
    cols = len(data[0])

    dp = defaultdict(int)
    st_row = 0
    for r, line in enumerate(data):
        if "S" in line:
            st_row = r
            dp[line.index("S")] = 1
            break
    exited = 0
    for r in range(st_row, rows):
        next_dp = defaultdict(int)
        for c, cnt in dp.items():
            ch = data[r][c]
            if ch == "^":
                if c - 1 >= 0:
                    next_dp[c - 1] += cnt
                else:
                    exited += cnt
                if c + 1 < cols:
                    next_dp[c + 1] += cnt
                else:
                    exited += cnt
            else:
                next_dp[c] += cnt
        dp = next_dp
    return exited + sum(dp.values())


def main():
    raw_input = read_input()
    data = parse_lines(raw_input)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
