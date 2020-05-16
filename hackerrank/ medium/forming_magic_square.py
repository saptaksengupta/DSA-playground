import sys
def formingMagicSquare(s):
    s = sum(s, [])
    magicSquares = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [4, 9, 2, 3, 5, 7, 8, 1, 6],
                    [6, 1, 8, 7, 5, 3, 2, 9, 4],
                    [2, 9, 4, 7, 5, 3, 6, 1, 8], [8, 3, 4, 1, 5, 9, 6, 7, 2],
                    [6, 7, 2, 1, 5, 9, 8, 3, 4], [4, 3, 8, 9, 5, 1, 2, 7, 6],
                    [2, 7, 6, 9, 5, 1, 4, 3, 8]]
    
    minCost = sys.maxsize

    for singleMag in magicSquares:
        diff = 0
        for (x, y) in zip(s, singleMag):
            diff += abs(x - y)
        minCost = min(minCost, diff)
    return minCost



demoS = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
print(formingMagicSquare(demoS))
