a = list(map(int, input().split()))
flag = 0
str1 = ""
for i in range(1, len(a)):
    if flag == 0:
        if a[i] != 0:
            str1 = str1 + str(i) + "0" * a[0] + str(i) * (a[i] - 1)
            flag = 1
    elif flag == 1:
        if a[i] != 0:
            str1 = str1 + str(i) * a[i]

print(str1)
