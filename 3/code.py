# Advent of code Year 2021 Day 3 solution
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

    gamma = ""
    for i in range(0, len(input[0].strip())):
        #print(i)
        for j in input:
        #    print(j.strip())
            d[str(j.strip()[int(i)])] += 1
        if d["0"] > d["1"]:
            gamma += "0"
        else:
            gamma += "1"
        #print(d)
        d["0"] = 0
        d["1"] = 0
    #print("bit" + str(bit))
    g = int(gamma, 2)

    epsilon = ""
    for b in gamma:
        if b == "1":
            epsilon += "0"
        else:
            epsilon += "1"
    e = int(epsilon, 2)
    return g * e

def solve2():
    values = input
    oxygen = ""
    for i in range(0, len(values[0].strip())):
        d = defaultdict(def_val)
        for j in values:
            d[str(j.strip()[int(i)])] += 1
        c = 0
        if d["0"] > d["1"]:
            c = "0"
        else: 
            c = "1"
        newinput = []
        for inp in values:
            if inp[i] == c:
                newinput.append(inp.strip())

        values = newinput
        if len(values) == 1:
            break

    oxygen = values[0]
    values = input
    for i in range(0, len(values[0].strip())):
        d = defaultdict(def_val)
        for j in values:
            d[str(j.strip()[int(i)])] += 1
        c = 0
        if d["0"] <= d["1"]:
            c = "0"
        else: 
            c = "1"
        newinput = []
        for inp in values:
            if inp[i] == c:
                newinput.append(inp.strip())

        values = newinput
        if len(values) == 1:
            break
    
    co = values[0]
    return int(oxygen, 2) * int(co, 2)
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))