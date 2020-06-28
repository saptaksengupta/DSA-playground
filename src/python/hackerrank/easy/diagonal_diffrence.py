
w, h = 3, 3
Matrix = [[0 for x in range(w)] for y in range(h)] 

Matrix[0][0] = 1
Matrix[0][1] = 8
Matrix[0][2] = 6
Matrix[1][0] = 2
Matrix[1][1] = 9
Matrix[1][2] = 3
Matrix[2][0] = 5
Matrix[2][1] = 12
Matrix[2][2] = 45

def diagonalDifference(demoArr):
    lToR1 = lToR2 = lToRCounter = rToLCounter = 0
    rToL1 = 0
    rToL2 = len(demoArr) - 1
    
    for x in range(len(demoArr)):
        lToRCounter = lToRCounter + demoArr[lToR1][lToR2]
        lToR1 += 1
        lToR2 += 1

        rToLCounter = rToLCounter + demoArr[rToL1][rToL2]
        rToL1 += 1
        rToL2 -= 1
    return abs(lToRCounter - rToLCounter)


print(diagonalDifference(Matrix))

