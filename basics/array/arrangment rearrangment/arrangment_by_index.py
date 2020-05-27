def arrange(arr):

    existedItems = set()
    for i in arr:
        existedItems.add(i)
    
    for x in range(len(arr)):
        if x in existedItems:
            arr[x] = x
        else:
            arr[x] = -1 

    return arr    

inputArray = input('Enter Elements: ').split()

inputArray = [int(x) for x in inputArray]

print(arrange(inputArray))

