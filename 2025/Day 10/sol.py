"""
author: UG_BEAST
"""

import re
import itertools


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


def solve_machine(line):
    lights_match = re.search(r"\[([.#]+)\]", line)
    lights_str = lights_match.group(1)
    num_lights = len(lights_str)

    target = 0
    for i, char in enumerate(lights_str):
        if char == "#":
            target |= 1 << i

    buttons = []
    button_groups = re.findall(r"\(([\d,]+)\)", line)
    for grp in button_groups:
        mask = 0
        for b_idx in grp.split(","):
            mask |= 1 << int(b_idx)
        buttons.append(mask)

    num_buttons = len(buttons)

    matrix = []
    rhs = []

    for r in range(num_lights):
        row_val = 0
        for c in range(num_buttons):
            if (buttons[c] >> r) & 1:
                row_val |= 1 << c
        matrix.append(row_val)
        rhs.append((target >> r) & 1)

    pivot_col_to_row = {}
    curr_row = 0

    for col in range(num_buttons):
        if curr_row >= num_lights:
            break

        pivot = -1
        for r in range(curr_row, num_lights):
            if (matrix[r] >> col) & 1:
                pivot = r
                break

        if pivot == -1:
            continue

        matrix[curr_row], matrix[pivot] = matrix[pivot], matrix[curr_row]
        rhs[curr_row], rhs[pivot] = rhs[pivot], rhs[curr_row]

        for r in range(num_lights):
            if r != curr_row and ((matrix[r] >> col) & 1):
                matrix[r] ^= matrix[curr_row]
                rhs[r] ^= rhs[curr_row]

        pivot_col_to_row[col] = curr_row
        curr_row += 1

    for r in range(curr_row, num_lights):
        if rhs[r] != 0:
            return float("inf")

    free_vars = [c for c in range(num_buttons) if c not in pivot_col_to_row]
    min_presses = float("inf")

    for free_vals in itertools.product([0, 1], repeat=len(free_vars)):
        solution = [0] * num_buttons

        for f_idx, val in zip(free_vars, free_vals):
            solution[f_idx] = val

        for c, r in pivot_col_to_row.items():
            val = rhs[r]
            for f_c in free_vars:
                if (matrix[r] >> f_c) & 1:
                    val ^= solution[f_c]
            solution[c] = val

        total_presses = sum(solution)
        if total_presses < min_presses:
            min_presses = total_presses

    return min_presses if min_presses != float("inf") else 0


def part1(data):
    ans = 0
    for line in data:
        result = solve_machine(line)
        ans += result
    return ans


def part2(data):
    result = 0
    return result


def main():
    raw_input = read_input()
    data = parse_lines(raw_input)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
