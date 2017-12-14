str1 = input()
str1 = str1.split()
N = int(str1[0])
P = int(str1[1])
b = input()
b = b.split()
for i in range(0, len(b)):
    b[i] = int(b[i])
b.sort()
MaxLength = 0
index = 0            #下标位置
Sum = 0              #统计允许的最大值和最小值之间的数量
flag = 0
for i in range(0, len(b)):
    if b[i] == b[i-1] and i != 0:   #若后面一个数与前一个数相等则跳过循环并且总数-1
        Sum -= 1
        continue
    Max = b[i]*P
    for j in range(index, len(b)):  #从当前下标开始循环
        index += 1
        if b[j] <= Max:
            Sum += 1
        if index == len(b):         #若下标已经移到末尾则修改标志量跳出两个循环
            flag = 1
            break
        if Max < b[j]:
            break
    if MaxLength < Sum:
        MaxLength = Sum
    if flag == 1:
        break
print(MaxLength)






#     for j in range(i, len(b)):
#         if b[i] <= b[j] <= Max:
#             Sum += 1
#         if Max < b[j]:
#             break
#     if MaxLength < Sum:
#         MaxLength = Sum
# print(MaxLength)
