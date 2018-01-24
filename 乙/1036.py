a = input().split()
N = int(a[0])
C = a[1]
column = N
if N % 2 != 0:
    row = N // 2 + 1
else:
    row = N / 2
for i in range(0, int(row)):
    if i == 0 or i == row - 1:
        print(C * column)
    else:
        print(C + " " * (column-2) + C)

