a = int(input())
flag2 = 0
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
verifier = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
for x in range(0, a):
    flag1 = 0
    Sum = 0
    b = input()
    for i in range(0, len(b) - 1):
        if b[i] < '0' or b[i] > '9':
            flag1 = 1
            flag2 = 1
            break
    if (b[17] < '0' or b[17] > '9') and b[17] != 'X':
        flag1 = 1
        flag2 = 1
    if flag1 == 1:
        print(b)
        flag2 = 1
        continue
    for i in range(0, 17):
        Sum += int(b[i]) * weight[i]
    if verifier[Sum % 11] == b[17]:
        continue
    else:
        print(b)
        flag2 = 1
        continue
if flag2 == 0:
    print("All passed")
