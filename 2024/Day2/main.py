def part1() -> int:
    inputs = []

    with open("2024/Day2/input.txt", "r") as file:
        for line in file:
            inputs.append([int(x) for x in line.strip().split(" ") if x])

    safe = 0
    for line in inputs:
        ascending = True
        prev = 0
        for i, num in enumerate(line):
            if i == 0:
                ascending = num < line[i + 1]
                prev = num
                continue
            if ascending:
                # if the number isnt ascending, break out of the loop
                if num <= prev or num - prev > 3:
                    break
                prev = num
            else:
                # if the number isnt descending, break out of the loop
                if num >= prev or prev - num > 3:
                    break
                prev = num

            if i == len(line) - 1:
                safe += 1

    return safe


def part2() -> int:
    inputs = []

    with open("2024/Day2/input.txt", "r") as file:
        for line in file:
            inputs.append([int(x) for x in line.strip().split(" ") if x])

    safe = 0
    for line in inputs:
        ascending = True
        prev = 0
        canSkip = True
        for i, num in enumerate(line):
            if i == 0:
                ascending = num < line[i + 1]
                prev = num
                continue
            if ascending:
                # if the number isnt ascending, break out of the loop
                if num <= prev or num - prev > 3:
                    if canSkip:
                        canSkip = False
                        continue
                    elif not canSkip:
                        if prev > num and num > line[i - 1] > line[i - 3]:
                            prev = num
                            continue

                    break
                prev = num
            else:
                # if the number isnt descending, break out of the loop
                if num >= prev or prev - num > 3:
                    if canSkip:
                        canSkip = False
                        continue
                    elif not canSkip:
                        if prev < num and num < line[i - 1] < line[i - 3]:
                            prev = num
                            continue
                    break
                prev = num

            if i == len(line) - 1:
                safe += 1

    return safe


def main() -> None:
    print(f"Part 1 result: {part1()}")
    print(f"Part 2 result: {part2()}")


if __name__ == "__main__":
    main()
