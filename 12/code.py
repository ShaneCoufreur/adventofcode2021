# Advent of code Year 2021 Day 12 solution
# Author = Shane Coufreur
# Date = December 2021
from collections import defaultdict

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

def def_val():
    return []

paths = defaultdict(def_val)

def solve_path_1(start, history):
    x = []
    y = history + [start]
    
    if start == "end":
        return [y]

    for neighbour in paths[start]:
        if neighbour != "start" and neighbour not in history or neighbour[0].isupper():
            z = solve_path_1(neighbour, y)
            x += z
    return x

def solve1():
    global paths
    paths = defaultdict(def_val)
    lines = [y.split("-") for y in [x.strip() for x in input]]
    for l in lines:
        start = l[0]
        end = l[1]
        paths[start].append(end)
        paths[end].append(start)

    return len(solve_path_1("start", []))

def solve_path_2(start, history):
    x = []
    y = history + [start]
    
    if start == "end":
        return [y]
    for neighbour in paths[start]:
        if neighbour != "start":
            if neighbour[0].isupper():
                z = solve_path_2(neighbour, y)
                x += z
            else:
                small_caves = [cave for cave in y if cave[0].islower()]
                visited_twice = False
                for c in small_caves:
                    if small_caves.count(c) > 1:
                        visited_twice = True
                        break
                if (visited_twice and y.count(neighbour) < 1) or (not visited_twice and y.count(neighbour) < 2):
                    z = solve_path_2(neighbour, y)
                    x += z
    return x

def solve2():
    global paths
    paths = defaultdict(def_val)
    lines = [y.split("-") for y in [x.strip() for x in input]]
    for l in lines:
        start = l[0]
        end = l[1]
        paths[start].append(end)
        paths[end].append(start)

    return len(solve_path_2("start", []))
    
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))