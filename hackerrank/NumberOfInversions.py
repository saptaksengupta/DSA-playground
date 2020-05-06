# arr = [1, 20, 6, 7, 5, 8, 11, 3]
# 1 3 5 2 4 6 7
arr = [7, 5, 3, 1]

numberOfInversions = 0

def getNumberOfInversionsCount(arrayToSort): 
    global numberOfInversions
    if len(arrayToSort) > 1:
        mid = len(arrayToSort) // 2
        left = arrayToSort[:mid]
        right = arrayToSort[mid:]
        
        getNumberOfInversionsCount(left)
        getNumberOfInversionsCount(right)

        # merging the list using two way merging technique.
        i = j = k = 0
        while (i < len(left) and j < len(right)):
            if left[i] <= right[j]:
                arrayToSort[k] = left[i]
                i += 1
            else:
                arrayToSort[k] = right[j]
                j += 1
                numberOfInversions += mid - i
            k = k + 1

        while i < len(left):
            arrayToSort[k] = left[i]
            i = i + 1
            k += 1

        while j < len(right):
            arrayToSort[k] = right[j]
            j = j + 1
            k += 1
    return numberOfInversions

# getNumberOfInversionsCount(arr)
# print(arr)
print(getNumberOfInversionsCount(arr))
    
        