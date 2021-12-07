# Advent of code Year 2021 Day 7 solution
# Author = Shane Coufreur
# Date = December 2021
import statistics

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

    inp = [int(x) for x in input[0].strip().split(",")]

def solve1():
    positions = inp.copy()

    pref_pos = int(statistics.median(positions))

    fuel_required = 0
    for i in positions:
        fuel_required += int(abs(pref_pos - i))
    
    return fuel_required

def solve2():
    positions = inp.copy()
    pref_pos = int(statistics.mean(positions))

    fuel_required = 0
    for i in positions:
        steps = abs(pref_pos - i)
        fuel_cost = round(steps * (steps +1) / 2)
        fuel_required += fuel_cost
    
    return fuel_required

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))