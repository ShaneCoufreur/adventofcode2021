# Advent of code Year 2021 Day 1 solution
# Author = Shane Coufreur
# Date = December 2021

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    inp = [int(i) for i in input]

def solve1():
    total_increments = 0
    for i in range(1, len(inp)):
        if inp[i] > inp[i-1]:
            total_increments += 1 
    return total_increments

def solve2():
    total_increments = 0
    last_sum = 0
    for ind, i in enumerate(range(2, len(inp))):
        sum = inp[i-2] + inp[i-1] + inp[i]
        
        if ind == 0:
            last_sum = sum
        else:
            if sum > last_sum:
                total_increments += 1
            last_sum = sum
    return total_increments

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))
