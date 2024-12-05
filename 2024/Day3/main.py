import re


def part1() -> int:

    regex = r"mul\((\d+),(\d+)\)"  # This is the regex pattern to match the multiplication function
    sum = 0

    with open("2024/Day3/input.txt", "r") as file:
        for line in file:
            matches = re.findall(regex, line)
            for match in matches:
                digit1, digit2 = map(int, match)
                sum += digit1 * digit2

    return sum


def part2() -> int:
    regex = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"  # This regex pattern matches do(), don't(), and mul() instructions
    sum = 0
    enabled = True  # At the beginning, mul instructions are enabled

    with open("2024/Day3/input.txt", "r") as file:
        for line in file:
            matches = re.findall(regex, line)
            for match in matches:
                instruction = match[0]
                if instruction == "do()":
                    enabled = True
                elif instruction == "don't()":
                    enabled = False
                elif enabled and match[1] and match[2]:
                    digit1, digit2 = int(match[1]), int(match[2])
                    sum += digit1 * digit2

    return sum


def main() -> None:
    print(f"Part 1 result: {part1()}")
    print(f"Part 2 result: {part2()}")


if __name__ == "__main__":
    main()
