from decimal import Decimal

def plusMinus(arr):
    posCount = neuCount = negCount = 0
    length = Decimal(len(arr))
    for i in range(len(arr)):
        if arr[i] > 0:
            posCount += 1
        elif arr[i] < 0:
            negCount += 1
        else: 
            neuCount += 1
    
    print(Decimal(posCount) / length)
    print(Decimal(negCount) / length)
    print(Decimal(neuCount) / length)


a = [-1, 1, 2, 3, 0, -2]
plusMinus(a)
            
