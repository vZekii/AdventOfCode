from time import sleep


def part1() -> int:
    obstacle_map = set()
    position = (0, 0)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up  # Right  # Down  # Left
    facing = 0
    board_size = (0, 0)
    with open("2024/Day6/input.txt", "r") as file:
        lines = file.readlines()
        board_size = (len(lines), len(lines[0]))
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == "#":
                    obstacle_map.add((i, j))
                elif char == "^":
                    position = (i, j)

        print(obstacle_map)
        print(board_size)

    distinct_positions = set()
    # while the guard is on the board
    while 0 <= position[0] < board_size[0] and 0 <= position[1] < board_size[1]:
        # if theres an obstacle in front of the guard, change direction
        if (
            position[0] + directions[facing][0],
            position[1] + directions[facing][1],
        ) in obstacle_map:
            facing = (facing + 1) % 4
            continue
        # otherwise move the guard forward
        position = (
            position[0] + directions[facing][0],
            position[1] + directions[facing][1],
        )
        distinct_positions.add(position)

    return len(distinct_positions)


# 5560 too high


def part2() -> int:
    with open("2024/Day6/input.txt", "r") as file:
        return 0


def main() -> None:
    print(f"Part 1 result: {part1()}")
    print(f"Part 2 result: {part2()}")


if __name__ == "__main__":
    main()
