a = input().split()
N = int(a[0])
signal = a[1]
Sum = 1
Max = 1
blank = 0

if N != 1:
    for i in range(6, 1000, 4):
        Sum += i
        if Sum >= N:
            Sum -= i
            Max = int((i - 4) / 2)
            break

for i in range(Max, 0, -2):
    print(" " * blank + signal * i)
    blank += 1
blank -= 1
for i in range(3, Max + 1, 2):
    blank -= 1
    print(" " * blank + signal * i)
print(N - Sum)
