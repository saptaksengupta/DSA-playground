def catAndMouse(x, y, z): 

    disA = abs(x - z)
    disB = abs(y - z)

    if disA < disB:
        print('Cat A')
    elif disA > disB:
        print('Cat B')
    else: 
        print('Mouse C')

q = int(input())

for x in range(q):
    xyz = input().split()

    x = int(xyz[0]) 

    y = int(xyz[1])

    z = int(xyz[2])
catAndMouse(x, y, z)
