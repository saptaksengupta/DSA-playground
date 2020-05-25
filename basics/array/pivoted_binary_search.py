def findPivot(arr, low, high): 
    mid = (low + high) // 2

    if high <= low:
        return -1

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    elif mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    elif arr[low] >= arr[high]:
        return findPivot(arr, mid + 1, high)
    return findPivot(arr, low, mid)


def pivotedBinarySearch(arr, key, low, high):
    pivot = findPivot(arr, 0, high)

    if pivot == -1:
        return binarySearch(arr, key, 0, high)
    
    if key == arr[pivot]:
        return pivot
    elif key > arr[low] and key < arr[pivot]: 
        return binarySearch(arr, key, low, pivot)
    return binarySearch(arr, key, pivot + 1, high)


def binarySearch(arr, key, low, high): 
    if high < low:
        return -1

    mid = low + (high - low) // 2
    if key == arr[mid]:
        return mid
    elif key < arr[mid]: 
        return binarySearch(arr, key, low, mid)
    return binarySearch(arr, key, mid + 1, high)


testArray = input('Enter an array: ').split()

testArray = [int(x) for x in testArray]

key = int(input())

index = pivotedBinarySearch(testArray, key, 0, len(testArray) - 1)

if index > 0:
    print('Found at index:', index)
else:
    print('Not Found')
    