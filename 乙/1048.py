key, num = input().split()
result = ""
numLen = len(num)
keyLen = len(key)
j = 1
if numLen - keyLen >= 0:
    key = '0' * (numLen - keyLen) + key
else:
    num = '0' * (keyLen - numLen) + num
for i in range(len(key) - 1, -1, -1):
    if j % 2 == 1:
        res = (int(key[i]) + int(num[i])) % 13
        if res == 10:
            result = "J" + result
        elif res == 11:
            result = "Q" + result
        elif res == 12:
            result = "K" + result
        else:
            result = str(res) + result
    else:
        res = int(num[i]) - int(key[i])
        if res < 0:
            result = str(res + 10) + result
        else:
            result = str(res) + result
    j += 1
print(result)
