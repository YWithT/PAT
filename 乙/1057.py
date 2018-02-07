string = input().lower()
Sum = 0
for i in string:
    if 'a' <= i <= 'z':
        Sum += ord(i) - ord('a') + 1
if Sum == 0:  # 防止当Sum=0时输出1,0
    print("0 0")
    exit()
Sum_bin = bin(Sum)
Sum_0 = 0
Sum_1 = 0
for i in range(2, len(Sum_bin)):
    if Sum_bin[i] == '0':
        Sum_0 += 1
    elif Sum_bin[i] == '1':
        Sum_1 += 1
print(str(Sum_0) + " " + str(Sum_1))
