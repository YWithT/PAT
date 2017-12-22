A, B, D = list(map(int, input().split()))
A = A + B
str1 = ""
while (A != 0):
    y = A % D
    A = A // D
    str1 = str(y) + str1

if str1 == "":
    print(0)
else:
    print(str1)
