"""
author: UG_BEAST
"""

import math


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


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            if self.size[rootA] < self.size[rootB]:
                rootA, rootB = rootB, rootA
            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]
            return True
        return False


def part1(data):
    result = 0
    coords = []
    for line in data:
        coords.append(list(map(int, line.split(","))))
    n = len(coords)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            pi = coords[i]
            pj = coords[j]
            distance = math.sqrt(
                abs(pi[0] - pj[0]) ** 2
                + abs(pi[1] - pj[1]) ** 2
                + abs(pi[2] - pj[2]) ** 2
            )
            edges.append((distance, (i, j)))

    edges.sort(key=lambda x: x[0])

    dsu = DSU(n)
    for k in range(1000):
        _, (i, j) = edges[k]
        dsu.union(i, j)

    comp_sizes = {}
    for i in range(n):
        root = dsu.find(i)
        comp_sizes[root] = comp_sizes.get(root, 0) + 1
    comp_sizes = sorted(comp_sizes.values(), reverse=True)
    result = comp_sizes[0] * comp_sizes[1] * comp_sizes[2]
    return result


def part2(data):
    result = 0
    coords = []
    for line in data:
        coords.append(list(map(int, line.split(","))))
    n = len(coords)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            pi = coords[i]
            pj = coords[j]
            distance = math.sqrt(
                abs(pi[0] - pj[0]) ** 2
                + abs(pi[1] - pj[1]) ** 2
                + abs(pi[2] - pj[2]) ** 2
            )
            edges.append((distance, (i, j)))

    edges.sort(key=lambda x: x[0])

    dsu = DSU(n)
    total_coponents = n
    for _, (u, v) in edges:
        if dsu.union(u, v):
            total_coponents -= 1

            if total_coponents == 1:
                x1 = coords[u][0]
                x2 = coords[v][0]

                result = x1 * x2
                break
    return result


def main():
    raw_input = read_input()
    data = parse_lines(raw_input)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
