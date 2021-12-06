# Advent of code Year 2021 Day 5 solution
# Author = Shane Coufreur
# Date = December 2021
import numpy

test = False

if test:
    params = ("testinput", 10)
else:
    params = ("input", 1000)

with open((__file__.rstrip("code.py")+str(params[0])+".txt"), 'r') as input_file:
    input = [line.strip() for line in input_file.readlines()]
    
    grid = numpy.zeros((params[1], params[1]))

def solve1():
    g = grid.copy()
    for line in input:
        #print(line)
        x,y = line.strip("").split("->")
        x1, y1 = [int(x) for x in x.strip().split(",")]
        x2, y2 = [int(y) for y in y.strip().split(",")]
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2)+1):
                    g[i][x1] += 1
            elif y1 == y2:
                for i in range(min(x1, x2), max(x1, x2)+1):
                    g[y1][i] += 1
        else:
            pass
    
    num = 0
    for ix, x in enumerate(g):
        for iy, y in enumerate(x):
            if g[ix][iy] > 1:
                num += 1
    return num

def solve2():
    g = grid.copy()
    for line in input:
        #print(line)
        x,y = line.strip("").split("->")
        x1, y1 = [int(x) for x in x.strip().split(",")]
        x2, y2 = [int(y) for y in y.strip().split(",")]
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2)+1):
                    g[i][x1] += 1
            elif y1 == y2:
                for i in range(min(x1, x2), max(x1, x2)+1):
                    g[y1][i] += 1
        else:
            xs = []
            ys = []
            if x1 < x2:
                for x in range(x1, x2+1):
                    xs.append(x)
            else:
                for x in reversed(range(x2, x1+1)):
                    xs.append(x)            

            if y1 < y2:
                for y in range(y1, y2+1):
                    ys.append(y)
            else:
                for y in reversed(range(y2, y1+1)):
                    ys.append(y)

            for i, v in enumerate(xs):
                g[ys[i]][xs[i]] += 1

    num = 0
    for ix, x in enumerate(g):
        for iy, y in enumerate(x):
            if g[ix][iy] > 1:
                num += 1
    print(g)
    return num

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))