a = input()
a = a.split()
a.reverse()
for x in range(0, len(a)):
    print(a[x], end="")
    if x != len(a) - 1:
        print(" ", end="")
