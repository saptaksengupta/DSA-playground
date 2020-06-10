def getSubArrayBounds(arr, givenSum):

    currSum = 0
    leftIndex = 0
    for i in range(0, len(arr)):
        currSum += arr[i]

        if currSum > givenSum:
            currSum -= arr[leftIndex]
            leftIndex += 1

        if currSum == givenSum:
            return [leftIndex + 1, i + 1]

    return -1


inputArr = input('Enter the array: ').split()
inputArr = [int(x) for x in inputArr]
givenSum = int(input('Enter Sum: '))

res = getSubArrayBounds(inputArr, givenSum)

if res == -1:
    print('No subarray found')
else:
    print('sub array bounds are: ', res)