"""
author: UG_BEAST
"""

import math


def read_input():
    with open("input.txt") as f:
        return f.read()


def parse_grid(data):
    lines = data.splitlines()
    if not lines:
        return []
    max_width = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_width) for line in lines]

    return [list(line) for line in padded_lines]


def solve_part2_block(columns):
    numbers = []
    operator = None

    for col in columns:
        digits = [char for char in col if char.isdigit()]
        if digits:
            num = int("".join(digits))
            numbers.append(num)
        for char in col:
            if char in ["+", "*"]:
                operator = char

    if operator == "+":
        return sum(numbers)
    elif operator == "*":
        if not numbers:
            return 0
        return math.prod(numbers)

    return 0


def part1(grid):
    w = len(grid[0])
    h = len(grid)

    ans = 0
    s = 0

    for x in range(w + 1):
        is_separator = (x == w) or all(grid[y][x] == " " for y in range(h))

        if is_separator:
            if x > s:
                block = []
                for y in range(h):
                    segment = "".join(grid[y][s:x]).strip()
                    if segment:
                        block.append(segment)
                if block:
                    all_text = ""
                    for y in range(h):
                        all_text += " " + "".join(grid[y][s:x])

                    tokens = all_text.split()
                    if tokens:
                        op = tokens[-1]
                        nums = list(map(int, tokens[:-1]))

                        if op == "+":
                            ans += sum(nums)
                        elif op == "*":
                            ans += math.prod(nums)

            s = x + 1

    return ans


def part2(grid):
    cols = list(zip(*grid))

    ans = 0
    curr = []

    for col in cols:
        if all(c == " " for c in col):
            if curr:
                ans += solve_part2_block(curr)
                curr = []
        else:
            curr.append(col)

    if curr:
        ans += solve_part2_block(curr)

    return ans


def main():
    raw_input = read_input()
    grid = parse_grid(raw_input)

    print("Part 1:", part1(grid))
    print("Part 2:", part2(grid))


if __name__ == "__main__":
    main()
