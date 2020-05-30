import sys

def partition(low, high):
    pivot = low
    i = low
    j = high
    while i <= j:
        while True:
            i += 1
            if inputArray[pivot] <= inputArray[i]:
                break
        
        while True: 
            j -= 1
            if inputArray[pivot] >= inputArray[j]: 
                break
        
        if i < j: 
            inputArray[i], inputArray[j] = inputArray[j], inputArray[i]
    
    inputArray[low], inputArray[j] = inputArray[j], inputArray[low]

    return j


def quickSort(low, high):

    if low < high:
        pIndex = partition(low, high)
        quickSort(low, pIndex)
        quickSort(pIndex + 1, high)


inputArray = input('Enter Elements: ').split()

inputArray = [int(x) for x in inputArray]

maxNumber = sys.maxsize

# when big boss comes into the picture
inputArray.append(maxNumber)
quickSort(0, len(inputArray) - 1)

# To eleminate big boss
inputArray.pop()
print(inputArray)

# 10 16 8 12 15 6 3 9 5