# Advent of code Year 2021 Day 9 solution
# Author = Shane Coufreur
# Date = December 2021
from collections import defaultdict

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

def find_up(grid, x, y):
    if x > 0:
        up = grid[x-1][y]
    else:
        up = 10
    return up

def find_down(grid, x, y):
    if x < len(grid)-1:
        down = grid[x+1][y]
    else:
        down = 10
    return down

def find_left(grid, x, y):
    if y > 0:
        left = grid[x][y-1]
    else:
        left = 10
    return left

def find_right(grid, x, y):
    if y < len(grid[0])-1:
        right = grid[x][y+1]
    else:
        right = 10
    return right

def solve1():
    grid = []

    for line in input:        
        grid.append([int(x) for x in line.strip()])

    lowpoints = []
    for x in range(len(grid)):
        #print("===============")
        for y in range(len(grid[0])):
            up = find_up(grid, x, y)
            down = find_down(grid, x, y)
            left = find_left(grid, x, y)
            right = find_right(grid, x, y)
                
            v = grid[x][y]
            if v < min(up, down, left, right):
                #print(v, (x, y), up, down, left, right)
                lowpoints.append(v+1)
    return sum(lowpoints)

def def_val():
    return False

def check_basin_size(x, y):
    count = 0
    if checked[(x, y)] == True:
        return 0
    else:
        checked[(x, y)] = True
        if grid[x][y] < 9:
            count += 1
        else:
            return 0

        #check up
        if x > 0:
            count += check_basin_size(x-1, y)
        #check down
        if x >= 0 and x < len(grid)-1:
            count += check_basin_size(x+1, y)

        #check left
        if y >= 0 and y < len(grid[0])-1:
            count += check_basin_size(x, y+1)

        #check right
        if y > 0:
            count += check_basin_size(x, y-1)
    return count

def solve2():
    global checked
    checked = defaultdict(def_val)
    global grid
    grid = []

    for line in input:        
        grid.append([int(x) for x in line.strip()])

    basins = []       
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            c = check_basin_size(x, y)
            if c > 0:
                basins.append(c)
    
    basins.sort()
    basins = list(reversed(basins))

    return basins[0] * basins[1] * basins[2]

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))