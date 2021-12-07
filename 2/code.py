# Advent of code Year 2021 Day 2 solution
# Author = Shane Coufreur
# Date = December 2021

from collections import defaultdict

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

def def_val():
    return 0

def solve1():
    #init default dictionary
    d = defaultdict(def_val)

    #split strings into tuple, sanitize
    inp = [(lambda x: (x[0], int(x[1])))(x.strip().split(" ")) for x in input]

    for i in inp:
        #if up, decrease depth
        if i[0] == "up":
            d["d"] -= i[1]
        #if down, increase depth
        elif i[0] == "down":
            d["d"] += i[1]
        #if forward, increase horizontal
        elif i[0] == "forward":
            d["h"] += i[1]
    return (d["d"], d["h"], d["d"]*d["h"])

def solve2():
    #init default dictionary
    d = defaultdict(def_val)

    #split strings into tuple, sanitize
    inp = [(lambda x: (x[0], int(x[1])))(x.strip().split(" ")) for x in input]
    for i in inp:
        #if up, decrease aim
        if i[0] == "up":
            d["a"] -= i[1]
        #if down, increase aim
        elif i[0] == "down":
            d["a"] += i[1]
        #if forward
        # - increase horizontal
        # - increase depth by aim * value
        elif i[0] == "forward":
            d["h"] += i[1]
            d["d"] += d["a"] * i[1] 
    return (d["d"], d["h"], d["d"]*d["h"])

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))