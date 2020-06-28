# You are given a sorted array containing only numbers 0 and 1. 
# Find the transition point efficiently. 
# Transition point is a point where "0" ends and "1" begins (0 based indexing).
# Note that, if there is no "1" exists, print -1.

def findTraPoint(arr, n):
    low = 0
    high = n - 1
    foundIndex = getTraIndex(arr, low, high)
    return foundIndex


def getTraIndex(arr, low, high):

    mid = low + (high - low) // 2
    
    if high - low >= 1: 

        if arr[mid + 1] != arr[mid] or arr[mid -1] != arr[mid]:
            return mid + 1

        if arr[low] == arr[mid]:
            return getTraIndex(arr, mid + 1, high)
        elif arr[mid] == arr[high]: 
            return getTraIndex(arr, low, mid)
    
    return -1

testArr = [0, 0, 0, 1, 1]
print(findTraPoint(testArr, len(testArr)))