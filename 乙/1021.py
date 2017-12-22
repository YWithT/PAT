a = input()
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range(0, len(a)):
    value = int(a[x])
    b[value] += 1

for i in range(0, len(b)):
    if b[i] != 0:
        print("%d:%d" % (i, b[i]))
