def getEqlIndex(arr):

    arrSum = 0
    leftSum = 0
    for i in range(len(arr)):
        arrSum += arr[i]
    
    for j in range(0, len(arr)):
        arrSum -= arr[j]

        if arrSum == leftSum:
            return j

        leftSum += arr[j]

    return j

inputArr = input('Enter the array: ').split()
inputArr = [int(x) for x in inputArr]

ind = getEqlIndex(inputArr)
print(ind)
