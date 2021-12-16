# Advent of code Year 2021 Day 13 solution
# Author = Shane Coufreur
# Date = December 2021
import numpy

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()


    dots = [dot.strip() for dot in input[:input.index('\n')]]
    instructions = [[ i[0][-1], int(i[1]) ] for i in [instr.strip().split("=") for instr in input[input.index('\n')+1:]]]

grid = []
def solve1():
    #init grid
    ys = [y[1] for y in instructions if y[0] == 'y']
    xs = [x[1] for x in instructions if x[0] == 'x']
    maxy = max(ys)*2+1
    maxx = max(xs)*2+1

    grid = numpy.zeros(shape=(maxy, maxx))

    #set dots
    for dot in dots:
        x, y = [int(xy) for xy in dot.split(',')]
        grid[y][x] = 1
    
    #handle instructions:
    for ins in [instructions[0]]:
        if ins[0] == 'x': #fold over x
            new_grid = numpy.zeros(shape=(len(grid), int((len(grid[0])-1) / 2)))
            for r, row in enumerate(grid):
                for c, col in enumerate(row):
                    if c < ins[1]:
                        new_grid[r][c] = int(max(  grid[r][c], grid[r][ (ins[1]+ins[1])-c ] ))
                    else:
                        break
        elif ins[0] == 'y': #fold over y
            new_grid = numpy.zeros(shape=(int((len(grid)-1) / 2), len(grid[0])))
            for r, row in enumerate(grid):
                if r < ins[1]:
                    for c, col in enumerate(row):
                        new_grid[r][c] = int(max(grid[r][c], grid[ (ins[1]+ins[1]-r) ][c]))
        grid = new_grid
    return sum(numpy.count_nonzero(grid, axis=0))

def solve2():
    #init grid
    ys = [y[1] for y in instructions if y[0] == 'y']
    xs = [x[1] for x in instructions if x[0] == 'x']
    maxy = max(ys)*2+1
    maxx = max(xs)*2+1

    grid = numpy.zeros(shape=(maxy, maxx))

    #set dots
    for dot in dots:
        x, y = [int(xy) for xy in dot.split(',')]
        grid[y][x] = 1
    
    #handle instructions:
    for ins in instructions:
        if ins[0] == 'x': #fold over x
            new_grid = numpy.zeros(shape=(len(grid), int((len(grid[0])-1) / 2)))
            for r, row in enumerate(grid):
                for c, col in enumerate(row):
                    if c < ins[1]:
                        new_grid[r][c] = int(max(  grid[r][c], grid[r][ (ins[1]+ins[1])-c ] ))
                    else:
                        break
        elif ins[0] == 'y': #fold over y
            new_grid = numpy.zeros(shape=(int((len(grid)-1) / 2), len(grid[0])))
            for r, row in enumerate(grid):
                if r < ins[1]:
                    for c, col in enumerate(row):
                        new_grid[r][c] = int(max(grid[r][c], grid[ (ins[1]+ins[1]-r) ][c]))
        grid = new_grid
    output = []
    for r, row in enumerate(grid):
        output.append([])
        for c, col in enumerate(row):
            c1 = ''
            if col == 1:
                c1 = '##'
            else:
                c1 = '  '
            output[r].append( c1 )
        print("".join(output[r]))
    return sum(numpy.count_nonzero(grid, axis=0))

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))