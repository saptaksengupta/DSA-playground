def whatFlavors(cost, money): 

    purchased = {}
    for i in range(len(cost)):
        diff = money - cost[i]
        if diff not in purchased:
            purchased.update({cost[i]: i + 1})
        else: 
            print(purchased[diff], i + 1)
    return -1



cost = input('enter money ').split()
cost = [int(x) for x in cost]
resp = whatFlavors(cost, 4)
