str1 = input()
num1 = input()
num2 = input()
result = ""
flag = 0
strLength = len(str1)
num1 = "0" * (strLength - len(num1)) + num1
num2 = "0" * (strLength - len(num2)) + num2
for i in range(strLength - 1, -1, -1):
    if int(num1[i]) + int(num2[i]) + flag >= (int(str1[i]) if int(str1[i]) != 0 else 10):
        result = str(int(num1[i]) + int(num2[i]) + flag - (int(str1[i]) if int(str1[i]) != 0 else 10)) + result
        flag = 1
    else:
        result = str(int(num1[i]) + int(num2[i]) + flag) + result
        flag = 0
if flag == 1:
    result = "1" + result
print(int(result))
