n = int(input())
m = list(map(int, input().split()))
m.sort(reverse=True)
E = 0
for i in range(n):
    if m[i] > i + 1:
        E += 1
    else:
        break
print(E)
