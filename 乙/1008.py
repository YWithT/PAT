a = input()
a = a.split()
N = int(a[0])
M = int(a[1])
b = input()
b = b.split()
for i in range(0, len(b)):
    b[i] = int(b[i])
for i in range(0, M):
    x = b.pop()
    b.insert(0, x)
for i in range(0, len(b)):
    print(b[i], end="")
    if i != len(b) - 1:
        print(" ", end="")
