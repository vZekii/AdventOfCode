def part1() -> int:
    # Part 1: Collect the first and last digits in a string, to create a 2 digit number. From there, sum all the numbers to get the answer

    sum = 0

    with open("./Day1/input.txt", "r") as file:
        for line in file:
            line = [n for n in line if n.isdigit()]
            num = line[0] + line[-1]
            sum += int(num)

    return sum


def part2() -> int:
    # Part 2: Some digits are spelled as a string but they still count as digits. Convert them and then find the sum

    sum = 0

    string_to_num = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }  # The extra parts on the string here are crazy

    with open("./Day1/input.txt", "r") as file:
        for line in file:
            for key, value in string_to_num.items():
                line = line.replace(key, value)
            line = [n for n in line if n.isdigit()]
            num = line[0] + line[-1]
            sum += int(num)

    return sum


def main() -> None:
    print(f"Part 1 result: {part1()}")
    print(f"Part 2 result: {part2()}")


if __name__ == "__main__":
    main()
