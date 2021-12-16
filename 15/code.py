# Advent of code Year 2021 Day 15 solution
# Author = Shane Coufreur
# Date = December 2021
import numpy as np
import networkx as nx

grid = np.genfromtxt("input.txt", delimiter=1, dtype=int)

def solve(g):
    graph = nx.DiGraph()

    for x in range(len(g)):
        for y in range(len(g)):
            if x < len(g)-1:
                graph.add_edge( (x,y), (x+1,y), weight=g[x+1][y] )
                graph.add_edge( (x+1,y), (x,y), weight=g[x][y] )
                
            if y < len(g)-1:
                graph.add_edge( (x,y), (x,y+1), weight=g[x][y+1] )
                graph.add_edge( (x,y+1), (x,y), weight=g[x][y] )

    s = 0

    for point in nx.shortest_path( graph, source=(0,0), target=(len(g)-1, len(g)-1), weight='weight'):
        s += g[point[0]][point[1]]
    
    #remove initial step cost
    s -= g[0][0]
        
    return s


def solve1():
    g = grid.copy()
    return solve(g)

def solve2():
    g = grid.copy()
    g1 = g.copy()
    for _ in range(4):
        g1 += 1
        g1[np.where(g1 == 10)] = 1
        g = np.concatenate((g, g1), axis=1)

    g1 = g.copy()
    for _ in range(4):
        g1 += 1
        g1[np.where(g1 == 10)] = 1
        g = np.concatenate((g, g1), axis=0)

    return solve(g)

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))