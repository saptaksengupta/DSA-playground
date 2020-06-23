def rotateArray(arr, d, n): 

    if d == 0:
        return

    reverseArray(arr, 0, d - 1)
    reverseArray(arr, d, n)
    reverseArray(arr, 0, n)


def reverseArray(arr, start, end):

    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    return



testArray = input('Enter an array: ').split()

numberOfRotation = int(input())

testArray = [int(x) for x in testArray]

rotateArray(testArray, numberOfRotation, len(testArray) - 1)

print(testArray)