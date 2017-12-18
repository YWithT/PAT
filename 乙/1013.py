import math


def isprime(x):  #验证是否为素数
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


a = input()
a = a.split()
a[0] = int(a[0])
a[1] = int(a[1])

Nums = list(range(0, 104730))
Flags = [True] * len(Nums)
Flags[0] = False
Flags[1] = False
Flags[2] = True
Sum = 1    #当前素数总数

for i in range(2, int(math.sqrt(len(Nums))) + 1):    #range的第二个参数应特别注意（素数的快速筛选法）
    if Flags[i]:
        if isprime(Nums[i]):
            Sum += 1
            if Sum >= a[1] and i > 2:    #若当前素数数量已达到要求则退出循环
                break
            for j in range(i + i, len(Nums), i):    #将目前素数在范围内的所有倍数均标记为False
                Flags[j] = False

Primes = []
for i in range(0, len(Nums)):   #将范围内的所有素数添加进新数列
    if Flags[i] == True:
        Primes.append(Nums[i])

step = 1
for i in range(a[0] - 1, a[1]):   #输出
    if step != 10 and i != a[1] - 1:
        step += 1
        print(str(Primes[i]) + " ", end="")
    elif step != 10 and i == a[1] - 1:
        step += 1
        print(str(Primes[i]), end="")
    else:
        step = 1
        print(str(Primes[i]))
