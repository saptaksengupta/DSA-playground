def reArrangeEvenOdd(arr):
    
    for i in range(0, len(arr) - 1, 2):
        # odd positions
        if arr[i] >= arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        
    
    if (len(arr) & 1):
        i = len(arr) - 1
        while i > 0:
            if arr[i] > arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 2
    return


inputArray = input('Enter Elements: ').split()

inputArray = [int(x) for x in inputArray]

reArrangeEvenOdd(inputArray)
print(inputArray)