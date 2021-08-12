a = [(3, 4), (1, 2), (4, 5), (2, 3)]
b = []

for i in range(len(a)):
    c = list(a[i])
    b.append(c)

for i in range(len(b)):
    for j in range(b[i][1] - b[i][0] + 1):
        b[i].append(j + b[i][0])
    b[i] = set(b[i])


def fun(b, j=0):
    if j >= len(b) - 1:
        return b
    for i in range(j + 1, len(b)):
        if set(b[i]) & set(b[j]):
            b[j] = sorted(list(set(b.pop(i)) | set(b[j])))
            return fun(b, j)
    return fun(b, j + 1)


fun(b)

for i in range(len(b)):
    b[i] = list(b[i])
    for j in range(len(b[i]) - 2):
        b[i].pop(1)
    b[i] = tuple(b[i])

print(b)
