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


def helper(target_length, data):
    n = len(data)
    rm_char = n - target_length
    stack = []
    for c in data:
        while stack and rm_char > 0 and stack[-1] < c:
            stack.pop()
            rm_char -= 1
        stack.append(c)
    ans = "".join(stack[:target_length])
    return int(ans)


def part1(data):
    # print(len(max(data)))     # maximum characters are 100 only
    ans = 0
    for i in data:
        maxi = helper(2, i)
        ans += maxi
    return ans
    # BRUTE FORCE APPROACH
    # for i in data:
    #     maxi = -1e9
    #     for l in range(len(i)):
    #         cur = str(i[l])
    #         for j in range(l, len(i)):
    #             if l == j:
    #                 continue
    #             if len(cur) >= 2:
    #                 cur = cur[:1]
    #             cur += i[j]
    #             maxi = max(maxi, int(cur))
    #     # print(f"{i}: {maxi}")
    #     ans += maxi


def part2(data):
    ans = 0
    for i in data:
        maxi = helper(12, i)
        ans += maxi
    return ans


def main():
    raw_input = read_input()
    data = parse_lines(raw_input)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
