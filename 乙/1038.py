n = input()
n1 = input().split()
n2 = input().split()
a = []
for i in range(1, int(n2[0]) + 1):
    a.append(str(n1.count(n2[i])))
print(" ".join(a))
