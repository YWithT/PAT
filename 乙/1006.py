def printS(x):
    for i in range(0, x):
        print("S", end="")


def printB(x):
    for i in range(0, x):
        print("B", end="")


def printG(x):
    for i in range(0, x):
        print(i + 1, end="")


a = input()
if len(a) == 1:
    x = int(a)
    printG(x)

if len(a) == 2:
    S = int(a[0])
    G = int(a[1])
    printS(S)
    printG(G)

if len(a) == 3:
    B = int(a[0])
    S = int(a[1])
    G = int(a[2])
    printB(B)
    printS(S)
    printG(G)
