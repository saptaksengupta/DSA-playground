
def slidingWindow(arr, windowRange):
    maxSum = 0
    windowSum = 0

    if len(arr) < windowRange:
        return None

    for x in range(0, windowRange):
        windowSum += arr[x]
        maxSum = windowSum

    for i in range(0, len(arr) - 1):

        if (windowRange + i) < len(arr):
            windowSum = windowSum - arr[i] + arr[windowRange + i]
            maxSum = max(windowSum, maxSum)
        
    return maxSum


inputArr = input('Enter the array: ').split()
inputArr = [int(x) for x in inputArr]
windowRange = int(input('enter Range: '))

maxSum = slidingWindow(inputArr, windowRange)

if maxSum == None: 
    print('There is no subarray of size', windowRange, 'as size of whole')
else: 
    print('Maximum Sum: ', maxSum)