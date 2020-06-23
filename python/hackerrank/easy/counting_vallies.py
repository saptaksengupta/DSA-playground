def countingValleys(n, s): 
    initialLevel = 0
    numberOfVallies = 0
    for i in range(0, len(s)):
        if s[i] == 'D':
            initialLevel -= 1
        else:
            initialLevel += 1

            if initialLevel == 0:
                numberOfVallies += 1
        
    return numberOfVallies


print(countingValleys(8, 'UDDDUDUU'))



