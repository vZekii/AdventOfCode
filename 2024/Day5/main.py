from collections import defaultdict
from collections import deque


def part1() -> int:

    rules = True
    rules_dict = defaultdict(set)
    sequences = []

    with open("2024/Day5/input.txt", "r") as file:
        for line in file:
            if line == "\n":
                rules = False
                continue
            if rules:
                rule = list(map(int, line.split("|")))
                rules_dict[rule[0]].add(rule[1])
            else:
                sequences.append(list(map(int, line.split(","))))

    sum = 0
    for sequence in sequences:
        middle = (len(sequence) - 1) // 2
        for i in range(1, len(sequence)):
            # only allow numbers that are in the list under the key of the number
            num = sequence[i]
            if num not in rules_dict[sequence[i - 1]] or num in rules_dict[sequence[i]]:
                i -= 1
                break
        if i == len(sequence) - 1:
            sum += sequence[middle]

    return sum


def part2() -> int:
    rules = True
    rules_dict = defaultdict(set)
    sequences = []

    with open("2024/Day5/input.txt", "r") as file:
        for line in file:
            if line == "\n":
                rules = False
                continue
            if rules:
                rule = list(map(int, line.split("|")))
                rules_dict[rule[0]].add(rule[1])
            else:
                sequences.append(list(map(int, line.split(","))))

    sum = 0
    for sequence in sequences:
        incorrect = False
        middle = (len(sequence) - 1) // 2
        for i in range(1, len(sequence)):
            # only allow numbers that are in the list under the key of the number
            num = sequence[i]
            if num not in rules_dict[sequence[i - 1]] or num in rules_dict[sequence[i]]:
                # mark as incorrect
                incorrect = True
                break

        if incorrect:
            graph = defaultdict(list)
            in_degree = defaultdict(int)
            nodes = set(sequence)

            for u in nodes:
                in_degree[u] = 0

            for u in nodes:
                for v in rules_dict[u]:
                    if v in nodes:
                        graph[u].append(v)
                        in_degree[v] += 1

            queue = deque([node for node in nodes if in_degree[node] == 0])
            sorted_sequence = []

            while queue:
                node = queue.popleft()
                sorted_sequence.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            sum += sorted_sequence[middle]

    return sum


def main() -> None:
    print(f"Part 1 result: {part1()}")
    print(f"Part 2 result: {part2()}")


if __name__ == "__main__":
    main()
