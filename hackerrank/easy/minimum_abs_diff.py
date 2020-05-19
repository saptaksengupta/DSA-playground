import sys


def minimumAbsoluteDifference(arr):
    arr.sort()
    lengthOfArray = len(arr)
    minAbsDiff = sys.maxsize
    for x in range(lengthOfArray - 1):
        print(abs(arr[x] - arr[x+1]))
        minAbsDiff = min(minAbsDiff, abs(arr[x] - arr[x + 1]))

    return minAbsDiff


myArr = input('Enter array: ').split()
myArr = [int(x) for x in myArr]

print(minimumAbsoluteDifference(myArr))
