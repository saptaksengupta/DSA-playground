
def pickingNumbers(a):
    frequecy = [0] * 101

    for i in range(len(a)):
        frequecy[a[i]] += 1
    
    result = 0
    for j in range(100):
        result = max(result, frequecy[j] + frequecy[j-1])
    
    return result



demoArr = input('Enter Array elements ').split()
demoArr = [int(x) for x in demoArr]
print(pickingNumbers(demoArr))