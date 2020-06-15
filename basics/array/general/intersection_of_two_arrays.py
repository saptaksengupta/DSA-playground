def findIntersection(a, b, n, m): 
    commonElements = {}
    res = []
    
    i = 0
    j = 0

    while i < n and j < m:
        # print(i, j)
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            if a[i] not in commonElements:
                commonElements.update({b[j]: True})
            i += 1
            j += 1

    for i in commonElements:
        res.append(i)

    if len(res) > 0:
        return res
    return -1

inputArr = input('Enter the array A: ').split()
inputArr = [int(x) for x in inputArr]

inputArrB = input('Enter the array B: ').split()
inputArrB = [int(x) for x in inputArrB]

commons = findIntersection(inputArr, inputArrB, len(inputArr), len(inputArrB))
print(commons)