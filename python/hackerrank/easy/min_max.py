# Given five positive integers, find the minimum and maximum values that can be calculated by 
# summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a 
# single line of two space-separated long integers.

# For example, . Our minimum sum is  and our maximum sum is . We would print

# 16 24

import sys

def miniMaxSum(arr):
    fullSum = 0
    for i in range(len(arr)):
        fullSum += arr[i]

    minSum = sys.maxsize
    maxSum = 0
    for j in range(len(arr)):
        minSum = min(minSum, fullSum - arr[j])
        maxSum = max(maxSum, fullSum - arr[j])


    print(minSum, maxSum)


myArr = input('Enter array: ').split()
myArr = [int(x) for x in myArr]

miniMaxSum(myArr)

