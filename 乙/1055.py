N, K = map(int, input().split())
peopel = []
result = []
name = []
for i in range(0, N):
    a = input().split()
    a[1] = int(a[1])
    peopel.append(a)
peopel.sort(key=lambda x: (-x[1], x[0]))
for i in range(0, N):
    name.append(peopel[i][0])
column = N // K
lastColumn = N - (N // K) * (K - 1)
name_new = ["0"] * len(name)
mid = lastColumn // 2
sign = 0
for i in range(0, lastColumn):
    name_new[mid + sign] = name[i]
    if sign >= 0:
        sign = -(sign + 1)
    else:
        sign = -sign
for i in range(0, K - 1):
    left = lastColumn + i * column
    right = lastColumn + (i + 1) * column
    mid = column // 2 + left
    sign = 0
    for j in range(left, right):
        name_new[mid + sign] = name[j]
        if sign >= 0:
            sign = -(sign + 1)
        else:
            sign = -sign
# print(name)
# print(name_new)

result.append(" ".join(name_new[0:lastColumn]))
for i in range(0, K - 1):
    result.append(" ".join(name_new[lastColumn + i * column:(i + 1) * column + lastColumn]))
for i in result:
    print(i)
