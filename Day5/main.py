seeds = []

with open("./Day5/input.txt", "r") as file:
    in_map = False
    convert = []
    for line_ind, line in enumerate(file):
        if line_ind == 0:
            initial_seeds = [int(s) for s in line.strip().split(" ")[1:]]
            for i in range(0, len(initial_seeds), 2):
                seeds += [
                    seed
                    for seed in range(
                        initial_seeds[i], initial_seeds[i] + initial_seeds[i + 1]
                    )
                ]
            print(seeds)
            quit()
            continue

        if "map" in line:
            in_map = True
            continue

        if in_map and line.strip() == "":
            in_map = False

            for i, seed in enumerate(seeds):
                print(i)
                for c in convert:
                    if c[1] <= seed <= c[1] + (c[2]):
                        print(f"found conversion {c} for seed {seed}")
                        seeds[i] = c[0] + (seed - c[1])
                        print(f"output {seeds[i]}")
                        break

            convert = []

            continue

        if in_map:
            convert.append([int(n) for n in line.strip().split(" ")])

seeds.sort()
print(seeds[0])
