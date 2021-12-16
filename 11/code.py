# Advent of code Year 2021 Day 11 solution
# Author = Shane Coufreur
# Date = December 2021
from itertools import product

with open((__file__.rstrip("code.py")+"testinput.txt"), 'r') as input_file:
    input = input_file.readlines()

grid = []
flashcount = 0
flashes = []
def handle_flashes():
    global flashcount
    while len(flashes) > 0:
        flashcount += 1
        i = flashes.pop(0)
        row = i[0]
        col = i[1]
        grid[row][col] = -1

        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                if r == 0 and c == 0:
                    continue
                
                r1 = row+r
                c1 = col+c

                if 0 <= r1 < len(grid) and 0 <= c1 < len(grid[0]) and grid[r1][c1] != -1:
                    grid[r1][c1] += 1
                    if grid[r1][c1] >= 10:
                        if (r1, c1 ) not in flashes:
                            flashes.append( (r1, c1) )

def solve1():
    global grid 
    grid = []
    global flashes
    global flashcount
    flashcount = 0
    for i in input:
        grid.append( [int(x) for x in i.strip()] )

    for i in range(100):
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                grid[row][column] += 1

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] > 9:
                    flashes.append(( row, column ))

        handle_flashes()
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == -1:
                    grid[row][column] = 0
    return flashcount

def solve2():
    global grid 
    grid = []
    global flashes
    for i in input:
        grid.append( [int(x) for x in i.strip()] )
    iterations = 0
    while True:
        iterations += 1
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                grid[row][column] += 1

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] > 9:
                    flashes.append(( row, column ))

        handle_flashes()
        c = True
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == -1:
                    grid[row][column] = 0
                else:
                    c = False
        if c:
            return iterations

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))