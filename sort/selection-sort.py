
import array

givenArr = array.array('i', [1, 3, 5, 2, 4, 6, 7])

def sortArray(arrayToSort):
    count = 0
    for i in range(len(arrayToSort) - 1):
        min = i
        for j in range(i + 1, len(arrayToSort)):
            if(arrayToSort[j] < arrayToSort[min]):
                min = j
        swapped = swapElement(arrayToSort, min, i)
        if(swapped):
            count += 1
    return count


def displayArrayElements(arrayToDisplay): 
    print("Sorted Array to display: ")
    for i in range(len(arrayToDisplay)):
        print(arrayToDisplay[i])

def swapElement(arr, indexA, indexB):
    temp = arr[indexB]
    arr[indexB] = arr[indexA]
    arr[indexA] = temp
    return True

minCount = sortArray(givenArr)
# displayArrayElements(givenArr)

print('Minimum number of swaps required:', minCount)