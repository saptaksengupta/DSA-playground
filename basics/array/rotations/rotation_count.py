def rotaitonCount(arr, low, high, n):


    if low > high:
        return 0
    
    if low == high:
        return low

    mid = low + (high - low) // 2
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid + 1
    
    if mid > low and arr[mid - 1] > arr[mid]:
        return mid

    if arr[mid] > arr[high]:
        return rotaitonCount(arr, mid + 1, high, n)
    return rotaitonCount(arr, low, mid, n)




inputArray = input('Enter Elements: ').split()

inputArray = [int(x) for x in inputArray]

rotations = rotaitonCount(inputArray, 0, len(inputArray) - 1, len(inputArray) - 1)

print(rotations, 'rotaions found!')
