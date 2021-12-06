# Advent of code Year 2021 Day 6 solution
# Author = Shane Coufreur
# Date = December 2021
from collections import defaultdict
from collections import Counter

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

    fishes = [int(x) for x in input[0].split(",")]

    print(fishes)

def solve1():
    fish = fishes.copy()

    for i in range(80):
        newfish = []
        for fi, f in enumerate(fish):
            if f == 0:
                f = 7
                newfish.append(8)

            f -= 1            
            fish[fi] = f
        fish.extend(newfish)
    
    #print(fish)
    print(Counter(fish))
    return len(fish)


def def_val():
    return 0

def solve2():
    fish = defaultdict(def_val)
    #print(fishes.copy())
    for f in fishes.copy():
        fish[f] += 1


    #loop through days
    for d in range(256):
        new_fish = defaultdict(def_val)
        # loop through items in collection

        for i in range(9):
            if i == 0:
                k = 7
                new_fish[8] += fish[i]
            else:
                k = i

            new_fish[k-1] += fish[i]
        fish = new_fish
    s = []
    for i in range(9):
        s.append(new_fish[i])

    return sum(s)


print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))