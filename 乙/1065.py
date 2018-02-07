N = int(input())
lovers = []
for i in range(0, N):
    a = input().split()
    lovers.append(int(a[0]))
    lovers.append(int(a[1]))
M = int(input())
guests = list(map(int, input().split()))
singles = []
for guest in guests:
    if guest not in lovers:
        singles.append(guest)
    else:
        index = lovers.index(guest)
        if index % 2 == 0:
            hisLove = lovers[index + 1]
        else:
            hisLove = lovers[index - 1]
        if hisLove not in guests:
            singles.append(guest)
singles.sort()
print(len(singles))
for i in range(0, len(singles)):
    if i != len(singles) - 1:
        print(singles[i], end=" ")
    else:
        print(singles[i])
