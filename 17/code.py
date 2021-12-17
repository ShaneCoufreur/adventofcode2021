# Advent of code Year 2021 Day 17 solution
# Author = Shane Coufreur
# Date = December 2021

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readline()
    x, y = [i.strip() for i in input[15:].split(",")]
    x1, x2 = [int(x) for x in x.split("..")]
    y = y.split("..")
    y[0] = y[0][2:]
    y1, y2 = [int(y) for y in y]

def solve1():
    # calculate max height
    # cheat a little by using Triangular Number equation
    return int(y1*(y1+1)/2)

def find_hits(vx, vy):
    hits = 0
    x, y = 0, 0

    toofar = False
    above = True

    while not toofar and above: #while we didn't overshoot, and we are still above the target
        if x <= x2 and x >= x1 and y >= y1 and y <= y2:
            hits += 1
            break

        x = x+vx
        y = y+vy

        # Due to gravity, the probe's y velocity decreases by 1.
        vy -= 1

        # Due to drag, the probe's x velocity changes by 1 toward the value 0; 
        #   that is, 
        #       it decreases by 1 if it is greater than 0, 
        #       increases by 1 if it is less than 0, 
        #       or does not change if it is already 0.
        if vx > 0: # we start at x = 0 so only implement decrease
            vx -= 1

        toofar = x > x2
        above = y >= y1

    return hits

def solve2():
    hits = 0

    for vx in range(x2 + 1):
        for vy in range(y1, -y1):
            hits += find_hits(vx, vy)

    return hits

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))