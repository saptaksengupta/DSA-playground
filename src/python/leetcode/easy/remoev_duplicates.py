def removeDuplicates(nums): 
    
    lastUniqueIndex = 1
    uniquCount = 1
    for i in range(0, len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[lastUniqueIndex] = nums[i + 1]
            uniquCount += 1
            lastUniqueIndex += 1

    return uniquCount


myArr = input('Enter array: ').split()
myArr = [int(x) for x in myArr]
print(removeDuplicates(myArr))
print(myArr)