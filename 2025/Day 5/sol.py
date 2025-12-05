"""
author: UG_BEAST
"""


def read_input():
    with open("input.txt") as f:
        return f.read().strip()


def parse_lines(data):
    parsed_queries = []
    parsed_range = []
    for line in data.splitlines():
        if not line:
            continue

        if "-" in line:
            start, end = line.split("-")
            parsed_range.append((int(start), int(end)))
        else:
            parsed_queries.append(int(line))

    parsed_data = [parsed_range, parsed_queries]
    return parsed_data


def part1(data):
    result = 0
    range_data, queries = data
    # print(len(queries))    # 1000 queries
    # print(len(max(data)))  # 14 LENGTH
    # print(len(range_data))  # 182
    # O(1000 * 182) -> 1e5 order -> acceptable
    for i in queries:
        for s, e in range_data:
            if s <= i <= e:
                result += 1
                break
    return result


def part2(data):
    result = 0
    range_data, _ = data
    # need to merge intervals
    range_data.sort()  # O(182log182) -> O(1)
    merged_intervals = []
    for s, e in range_data:
        if not merged_intervals or merged_intervals[-1][1] < s:
            merged_intervals.append([s, e])
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], e)
    for s, e in merged_intervals:
        result += e - s + 1
    return result


def main():
    raw_input = read_input()
    data = parse_lines(raw_input)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
