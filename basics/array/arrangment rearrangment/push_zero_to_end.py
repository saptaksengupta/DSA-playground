def pushZerosToTheEnd(arr):

    count = 0

    for i in range(len(arr)):
        if (arr[i] != 0):
            arr[count], arr[i] = arr[i], arr[count]
            count += 1


inputArray = input('Enter Elements: ').split()

inputArray = [int(x) for x in inputArray]

pushZerosToTheEnd(inputArray)
print(inputArray)