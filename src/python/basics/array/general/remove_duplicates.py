import array

def removeDuplicates(arr):
    items = set()
    for i in range(len(arr)):
        if arr[i] not in items:
            items.add(arr[i])

    freshArr = []
    for j in items:
        freshArr.append(int(j))

    return freshArr


inputArr = input('Enter the array: ').split()
inputArr = [int(x) for x in inputArr]

freshArr = removeDuplicates(inputArr)
print(freshArr)