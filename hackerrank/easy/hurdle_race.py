def hurdleRace(k, height):
    maxHeight = height[0]
    for x in range(1, len(height)):
        if height[x] > maxHeight:
            maxHeight = height[x]
    

    if k > maxHeight:
        return 0
    else:
        return abs(maxHeight - k)
    

print(hurdleRace(9, [1, 4, 8, 9]))




