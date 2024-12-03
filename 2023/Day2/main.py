def check_colors(games):
    for game in games:
        colors = game.split(", ")
        for color in colors:
            num, color = color.split(" ")
            if color_nums[color] < int(num):
                return False

    return True


sum = 0

color_nums = {"red": 12, "green": 13, "blue": 14}

with open("./Day2/input.txt", "r") as file:
    for line in file:
        line = line.rstrip().split(": ")
        ID = line[0].split(" ")[-1]

        games = line[1].split("; ")
        if check_colors(games):
            sum += int(ID)

print(sum)


# part 2


def check_colors(games):
    min = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        colors = game.split(", ")
        for color in colors:
            num, color = color.split(" ")
            if min[color] < int(num):
                min[color] = int(num)

    return min["red"] * min["blue"] * min["green"]


sum = 0

with open("./Day2/input.txt", "r") as file:
    for line in file:
        line = line.rstrip().split(": ")
        ID = line[0].split(" ")[-1]

        games = line[1].split("; ")
        sum += check_colors(games)

print(sum)
