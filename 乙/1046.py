N = int(input())
jia = yi = 0
for i in range(0, N):
    a = list(map(int, input().split()))
    if a[1] == a[0] + a[2] and a[1] != a[3]:
        yi += 1
    elif a[3] == a[0] + a[2] and a[3] != a[1]:
        jia += 1
print(str(jia) + " " + str(yi))
