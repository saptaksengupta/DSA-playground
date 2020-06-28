def birthdayCakeCandles(ar):

    tallest = 0
    tallestCountMap = {}

    for i in range(0, len(ar)):

        if ar[i] not in tallestCountMap:
            tallestCountMap.update({ar[i]: 1})
        else:
            newCount = tallestCountMap.get(ar[i]) + 1
            tallestCountMap.update({ar[i]: newCount})
        
        if ar[i] > tallest:
            tallest = ar[i]

    return tallestCountMap.get(tallest)


myArr = input('Enter array: ').split()
myArr = [int(x) for x in myArr]

print(birthdayCakeCandles(myArr))
