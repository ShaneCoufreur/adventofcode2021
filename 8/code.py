# Advent of code Year 2021 Day 8 solution
# Author = Shane Coufreur
# Date = December 2021
from collections import defaultdict

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

def def_val():
    return None

known = defaultdict(def_val)
known[2] = "1"
known[3] = "7"
known[4] = "4"
known[7] = "8"

def solve1():
    count = 0
    for inp in input:
        _, output = inp.split("|")
        out = output.split()

        for o in out:
            l = len(o)
            if l in known.keys():
                count += 1
    return count  

def overlap(a, b):
    s = 0
    for x in a:
        if x in b:
            s += 1

    return s
    
def determine_char(o, one, four):
    v = ""
    val = known[len(o)]
    if val != None:
        v += val
    elif len(o) == 5:
        # 2, 3 or 5
        if overlap(o, one)==2:
            v += "3"
        elif overlap(o, four)==2:
            v += "2"
        else:
            v += "5"
    elif len(o) == 6:
        # 9, 6 or 0
        if overlap(o, four)==4:
            v += "9"
        elif overlap(o, one)==2:
            v += "0"
        else:
            v += "6"
    return v

def solve2():
    total = 0
    for i in input:
        inp, out = [x.strip().split() for x in i.split("|")]

        one = ""
        four = ""
        for val in inp+out:
            if len(val) == 2:
                one = val
            elif len(val) == 4:
                four = val

        v = ""
        for o in out:
            v += determine_char(o, one, four)
        total += int(v)
    return total

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))