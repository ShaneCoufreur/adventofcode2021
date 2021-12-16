# Advent of code Year 2021 Day 14 solution
# Author = Shane Coufreur
# Date = December 2021
from collections import defaultdict

with open((__file__.rstrip("code.py")+"testinput.txt"), 'r') as input_file:
    input = input_file.readlines()

    template = input[0].strip()
    temp = [c.split('->') for c in [rule.strip().replace(' ', '') for rule in input[2:]]]

    rules = {}
    for rule in temp:
        rules[rule[0]] = rule[1]

#    print(template)
#    print(rules)
def def_val():
    return 0

def solve(iterations):
    polymer = defaultdict(def_val)

    #define the initial polymer
    # NNCB becomes
    # NN: 1
    # NC: 1
    # CB: 1
    for i in range(len(template)-1):
        polymer[template[i]+template[i+1]] += 1

    #iterate 10 times
    for i in range(iterations):
        new_polymer = defaultdict(def_val)
        for pol in polymer.keys():
            if pol in rules.keys(): #if pol found in rules, split set and app- and pre-pend the rule value
                # NN -> C
                # becomes NC and CN
                new_polymer[ pol[0] + rules[pol] ] += polymer[pol]
                new_polymer[ rules[pol] + pol[1] ] += polymer[pol]
        polymer = new_polymer
    
    occurence = defaultdict(def_val)
    #for all pairs add the count to the 2nd char key
    # NNCB
    # NN[1] -> N += 1
    # NC[1] -> C += 1
    # CB[1] -> B += 1
    for k in polymer.keys():
        occurence[k[1]] += polymer[k]
    
    #don't forget the first char
    #NN above
    occurence[list(polymer.keys())[0][0]] += 1

    v = list(occurence.values())
    v.sort()
    return max(v) - min(v)

def solve1():
    return solve(10)

def solve2():
    return solve(40)

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))