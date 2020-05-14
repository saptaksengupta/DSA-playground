def staircase(n):
    for i in range(1, n+1):
        breakPoint = n - i
        for j in range(0, breakPoint):
            print(" ", end='')
        for k in range(breakPoint, n):
            print("#", end='')
        print()

staircase(6)
