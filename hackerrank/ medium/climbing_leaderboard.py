def climbingLeaderboard(scores, alice):
    n = len(scores)
    m = len(alice)
    rank = [0] * n 
    positions = [0] * m

    rank[0] = 1
    for i in range(1, n):
        if scores[i] == scores[i - 1]:
            rank[i] = rank[i - 1]
        else:
            rank[i] = rank[i -1] + 1

    for y in range(m):
        if alice[y] >= scores[0]:
            positions[y] = 1
        elif alice[y] <= scores[len(scores) - 1]:
            positions[y] = rank[n - 1] + 1 
        else:
            expIndex = binarySearchForIndex(scores, alice[y])
            positions[y] = rank[expIndex]

    return positions


def binarySearchForIndex(scoresArray, score):
    low = 0
    high = len(scoresArray) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if scoresArray[mid] == score:
            return mid
        elif score > scoresArray[mid] and score < scoresArray[mid - 1]:
            return mid
        elif score < scoresArray[mid] and score > scoresArray[mid + 1]:
            return mid + 1
        elif score > scoresArray[mid]:
            high = mid - 1
        elif score < scoresArray[mid]:
            low = mid + 1

    return -1


scores = input('enter scores ').split()
scores = [int(x) for x in scores]
print(climbingLeaderboard(scores, [100, 85, 50, 10]))