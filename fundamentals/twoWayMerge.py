
a = [1, 3, 6, 25]
b = [4, 10, 11, 13]

def twoWayMerge(a, b, m, n): 
    i = j = k = 0
    c = []

    while (i < m and j < n):
        if a[i] < b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1
        k = k + 1

    while i < m: 
        c.append(a[i])
        i = i + 1

    while j < n: 
        c.append(b[j])
        j = j + 1

    return c

print(twoWayMerge(a, b, 4, 4))