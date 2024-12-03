total = 0

with open("./Day4/input.txt", "r") as file:
    for line in file:
        score = 0
        line = line.rstrip("\n")
        card, info = line.split(": ")

        winners, numbers = info.split(" | ")
        winners = [w.strip() for w in winners.split(" ") if w != ""]
        numbers = [n.strip() for n in numbers.split(" ") if n != ""]

        for num in numbers:
            if num in winners:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        total += score

print(total)


# part 2

total = 0

from collections import defaultdict

cards_won = defaultdict(int)

with open("./Day4/input.txt", "r") as file:
    for line in file:
        score = 0
        line = line.rstrip("\n")
        card, info = line.split(": ")

        cardnum = int(card.split(" ")[-1].strip())
        print(cardnum)

        cards_won[cardnum] += 1

        winners, numbers = info.split(" | ")
        winners = [w.strip() for w in winners.split(" ") if w != ""]
        numbers = [n.strip() for n in numbers.split(" ") if n != ""]

        for i in range(cards_won[cardnum]):
            next = cardnum + 1
            for num in numbers:
                if num in winners:
                    cards_won[next] += 1
                    next += 1


for card, value in cards_won.items():
    total += value

print(total)
