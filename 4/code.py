# Advent of code Year 2021 Day 4 solution
# Author = Shane Coufreur
# Date = December 2021

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

    draws = [int(draw) for draw in input[0].strip().split(",")]

    origboards = []
    for line in input[1:]:
        if line == "\n":
            board = []
            origboards.append(board)
        else:
            board.append([int(n) for n in line.strip().split()])

def solve1():
    winners = []
    lastdraw = 0
    boards = origboards.copy()
    for draw in draws:
        lastdraw = draw
        for board in boards:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == draw:
                        board[i][j] = -1

            #check rows
            for i in range(len(board)):
                if sum(board[i]) == -5:
                    winners.append(board)
                    break
            #check columns
            for j in range(len(board)):
                s = 0
                for i in range(len(board)):
                    s += board[i][j-1]
                if s == -5:                    
                    winners.append(board)
                    break

        if len(winners) > 0:
            break
        
    for winner in winners:
        s = 0
        for i in range(len(winner)):
            for j in range(len(winner[i])):
                s += max(0, winner[i][j])
        
        return s * lastdraw

def solve2():
    winners = []
    boards = origboards.copy()
    notyetwon = boards.copy()

    lastboardtowin = ()
    for draw in draws:
        lastdraw = draw
        for indx, board in enumerate(boards):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == draw:
                        board[i][j] = -1

            #check rows
            rowfound = False
            if rowfound == False:
                for i in range(len(board)):
                    if sum(board[i]) == -5:
                        if board in notyetwon:
                            winners.append(board)
                            notyetwon.remove(board)
                            lastboardtowin = (board, draw)
                        rowfound = True
                        break

            #check columns            
            if rowfound == False:
                for j in range(len(board)):
                    s = 0
                    for i in range(len(board)):
                        s += board[i][j-1]
                        if s == -5:                
                            if board in notyetwon:    
                                winners.append(board)
                                notyetwon.remove(board)
                                lastboardtowin = (board, draw)                
                            rowfound = True
                            break

        if len(notyetwon) == 0:
            break

    for winner in [lastboardtowin[0]]:
        s = 0
        for i in range(len(winner)):
            for j in range(len(winner[i])):
                s += max(0, winner[i][j])
        print( s, lastdraw )
        return s * lastdraw

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))