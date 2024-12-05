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

    def is_safe(levels):
        # Check if the levels are all increasing or decreasing with differences of 1-3
        increasing = all(
            1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1)
        )
        decreasing = all(
            1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1)
        )
        return increasing or decreasing

    with open("2024/Day2/input.txt", "r") as file:
        for line in file:
            inputs.append(list(map(int, line.split())))

    safe_count = 0
    for report in inputs:
        if is_safe(report):
            safe_count += 1
        else:
            # Check if removing one level makes it safe
            for i in range(len(report)):
                new_report = report[:i] + report[i + 1 :]  # Remove the i-th level
                if is_safe(new_report):
                    safe_count += 1
                    break  # Only need one valid removal to count as safe

    return safe_count


def main() -> None:
    print(f"Part 1 result: {part1()}")
    print(f"Part 2 result: {part2()}")


if __name__ == "__main__":
    main()
