arr = [9, 3, 5, 19, 45, 2, 6, 7, 1]

def mergeSort(arrayToSort): 
    
    if len(arrayToSort) > 1:
        mid = len(arrayToSort) // 2
        left = arrayToSort[:mid]
        right = arrayToSort[mid:]
        
        mergeSort(left)
        mergeSort(right)

        # merging the list using two way merging technique.
        i = j = k = 0
        while (i < len(left) and j < len(right)):
            if left[i] < right[j]:
                arrayToSort[k] = left[i]
                i += 1
            else:
                arrayToSort[k] = right[j]
                j += 1
            k = k + 1

        while i < len(left):
            arrayToSort[k] = left[i]
            i = i + 1
            k += 1

        while j < len(right):
            arrayToSort[k] = right[j]
            j = j + 1
            k += 1

mergeSort(arr)
print(arr)
    
        