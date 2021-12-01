#!/usr/bin/env python3


def part1(input1):
    return sum([1 for i, x in enumerate(input1[1:], start=1) if x > input1[i-1]])

def part2(input1, step):
    ticker = 0
    windows = [input1[i-step:i] for i in range(step - 1, len(input1))]
    for i, window in enumerate(windows[1:], start = 1):
        #print(sum(window), sum(windows[i-1]))
        if sum(window) > sum(windows[i-1]):
            ticker += 1
    return ticker

def main():
    with open("/workspace/aoc2021/day1/input1.txt", "r") as f:
        lines = [int(line) for line in f.read().splitlines()]
    print("Day 1, Solution 1: ", part1(lines))
    print("Day 1, Solution 2: ", part2(lines, 3))


if __name__ == "__main__":
    main()
