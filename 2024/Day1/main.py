from collections import Counter


def part1() -> int:
    distance = 0
    larr, rarr = [], []

    with open("2024/Day1/input.txt", "r") as file:
        for line in file:
            line = line.strip().split()
            larr.append(int(line[0]))
            rarr.append(int(line[-1]))

        larr.sort()
        rarr.sort()

        for i in range(len(larr)):
            distance += abs(larr[i] - rarr[i])
    return distance


def part2() -> int:
    similarity = 0
    larr, rarr = [], []
    with open("2024/Day1/input.txt", "r") as file:
        for line in file:
            line = line.strip().split()
            larr.append(int(line[0]))
            rarr.append(int(line[-1]))

    rarrc = Counter(rarr)
    for i, num in enumerate(larr):
        similarity += larr[i] * rarrc[num]

    return similarity


def main() -> None:
    print(f"Part 1 result: {part1()}")
    print(f"Part 2 result: {part2()}")


if __name__ == "__main__":
    main()
