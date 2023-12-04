grid = []

with open("./Day3/input.txt", "r") as file:
    for line in file:
        grid.append(list(line.replace("\n", "")))

total = 0

checks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for column_ind, line in enumerate(grid):
    in_num = False
    valid = False
    num = ""
    for row_ind, chara in enumerate(line):
        if chara in "0123456789":
            in_num = True
            num += chara

        elif in_num and chara not in "0123456789":
            in_num = False
            if valid:
                print("adding: ", num)
                total += int(num)
            valid = False
            num = ""

        if in_num and not valid:
            # scan around
            for c, r in checks:
                # Leetcode came in handy with this dfs constraint code
                if 0 <= column_ind + c < len(grid) and 0 <= row_ind + r < len(grid[0]):
                    check_chara = grid[column_ind + c][row_ind + r]
                    if check_chara not in ".0123456789":
                        valid = True
                        break

    # This took like 3 hours to figure out - newlines end the number, but they weren't being added because there was never technically an end
    if num != "" and in_num and valid:
        total += int(num)

print(total)
