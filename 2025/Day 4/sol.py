"""
author: UG_BEAST
"""


def main():
    with open("input.txt") as f:
        data = [line.strip() for line in f if line.strip()]

    r = len(data)
    c = len(data[0])

    grid = ["." * (c + 2)]
    for line in data:
        grid.append("." + line + ".")
    grid.append("." * (c + 2))

    m, n = r + 2, c + 2

    neighbors_cnt = [[0] * n for _ in range(m)]
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    dkg = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@":
                cnt = 0
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if grid[ni][nj] == "@":
                        cnt += 1
                neighbors_cnt[i][j] = cnt
                dkg.append((i, j))

    queue = []
    vis = set()

    part_1 = 0
    for i, j in dkg:
        if neighbors_cnt[i][j] < 4:
            part_1 += 1
            queue.append((i, j))
            vis.add((i, j))
    print("Part 1:", part_1)

    # part 2:
    part_2 = 0
    while queue:
        i, j = queue.pop(0)
        part_2 += 1
        for dx, dy in dirs:
            ni, nj = i + dx, j + dy
            if (ni, nj) in vis or grid[ni][nj] != "@":
                continue
            neighbors_cnt[ni][nj] -= 1
            if neighbors_cnt[ni][nj] < 4:
                queue.append((ni, nj))
                vis.add((ni, nj))
    print("Part 2:", part_2)


if __name__ == "__main__":
    main()


""""""

"""
NERD APPROACH

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


def part1(grid):
    result = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@":
                cnt = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "@":
                            cnt += 1
                if cnt < 4:
                    result += 1
    return result


def part2(grid):
    result = 0
    dkg = [[1 if ch == "@" else 0 for ch in row] for row in grid]
    m = len(dkg)
    n = len(dkg[0])
    # parse the dkg grid until I can get some element with neighbors < 4
    # and if I don't find any, I stop
    flag = 1
    while flag:
        flag = 0
        for i in range(m):
            for j in range(n):
                if dkg[i][j] == 1:
                    cnt = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue
                            ni, nj = i + dx, j + dy
                            if 0 <= ni < m and 0 <= nj < n and dkg[ni][nj] == 1:
                                cnt += 1
                    if cnt < 4:
                        dkg[i][j] = 0
                        result += 1
                        flag = 1
    return result


def main():
    raw_input = read_input()
    data = parse_lines(raw_input)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
"""
