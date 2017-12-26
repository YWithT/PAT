a, b = map(int, input().split())
b = b - a
s = b % 100
if s >= 50:
    s = int(b / 100) + 1
else:
    s = int(b / 100)

h = s // 3600
s = s % 3600
m = s // 60
s = s % 60
print("%02d:%02d:%02d" %(h, m, s))
