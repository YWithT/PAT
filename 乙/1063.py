import math

N = int(input())
Max = 0
for i in range(0, N):
    x, y = map(int, input().split())
    Max = max(Max, math.sqrt(x ** 2 + y ** 2))
print("%.2f" % Max)
