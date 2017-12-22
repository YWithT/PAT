a = input().split("E")
base = a[0]  # 底数（含符号）
index = a[1]  # 指数（含符号）
baseSignal = a[0][0]  # 底数符号
indexSignal = a[1][0]  # 指数符号
index = abs(int(index))  # 指数绝对值
base = list(base)
del base[0]  # 删除字符串中的符号

if indexSignal == "-":
    for i in range(0, index):
        if base.index(".") == 0:
            base[1] = "0" + base[1]
        else:
            dIndex = base.index(".")
            base[dIndex] = base[dIndex - 1]
            base[dIndex - 1] = "."
            if dIndex - 1 == 0:
                base[1] = ("".join(base[1:len(base)]))      #若一直用列表操作会超时，当小数点移动到边界后改用字符串操作
                del base[2:len(base)]

if indexSignal == "-" and base.index(".") == 0:
    base.insert(0, "0")

if indexSignal == "+":
    for i in range(0, index):
        if base.index(".") == len(base) - 1:
            base[0] = base[0] + "0"
        else:
            dIndex = base.index(".")
            base[dIndex] = base[dIndex + 1]
            base[dIndex + 1] = "."
            if dIndex + 1 == len(base) - 1:          #若一直用列表操作会超时，当小数点移动到边界后改用字符串操作
                base[0] = ("".join(base[0:len(base) - 1]))
                base[1] = "."
                del base[2:len(base)]

if indexSignal == "+" and base.index(".") == len(base) - 1:
    base.pop()

if baseSignal == "-":  # 若底数为负数则添加负号
    base.insert(0, "-")
print("".join(base))

#网上更好的解法
# import re
# s=re.compile("E")
# n=input()
# m=s.split(n)
# a=m[0]
# b=int(m[1])
# if a[0]=="+":
#     c=""
# else:
#     c="-"
# if b<0:
#     print(c+"0."+"0"*(abs(b)-1)+a[1:2]+a[3:])
# elif b==0:
#     print(c+a[1:])
# elif 0<b<len(a[3:]):
#     print(c+a[1]+a[3:b+3]+"."+a[b+3:])
# elif b==len(a[3:]):
#     print(c+a[1]+a[3:])
# elif b>len(a[3:]):
#     print(c+a[1]+a[3]+"0"*(b-len(a[3:])))