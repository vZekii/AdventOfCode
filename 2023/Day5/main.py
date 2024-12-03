seeds = []

with open("./Day5/input.txt", "r") as file:
    in_map = False
    convert = []
    for line_ind, line in enumerate(file):
        if line_ind == 0:
            initial_seeds = [int(s) for s in line.strip().split(" ")[1:]]

        if "map" in line:
            in_map = True
            continue

        if in_map and line.strip() == "":
            in_map = False

            for i, seed in enumerate(seeds):
                for c in convert:
                    if c[1] <= seed <= c[1] + (c[2]):
                        seeds[i] = c[0] + (seed - c[1])
                        break

            convert = []

            continue

        if in_map:
            convert.append([int(n) for n in line.strip().split(" ")])

seeds.sort()
print(seeds[0])
