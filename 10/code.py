# Advent of code Year 2021 Day 10 solution
# Author = Shane Coufreur
# Date = December 2021

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

pairs = ["()", "[]", "{}", "<>"]
right = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
def solve1():
    lines = [line.strip() for line in input]

    score = 0
    for l in lines:
        c = True
        while c:
            if any(pair in l for pair in pairs):
                for pair in pairs:
                    l = l.replace(pair,'')
            else:
                c = False
        for c in l:
            if c in right.keys():
                score += right[c]
                break

    return score

left = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}
def solve2():
    lines = [line.strip() for line in input]
    scores = []
    for l in lines:
        score = 0
        c = True
        while c:
            if any(pair in l for pair in pairs):
                for pair in pairs:
                    l = l.replace(pair,'')        
            else:
                c = False
                
        if not any(x in l for x in right.keys()):
            for c in reversed(l):
                score = score * 5
                score += left[c]
            scores.append(score)

    scores.sort()

    return scores[ int(len(scores) / 2) ]

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))