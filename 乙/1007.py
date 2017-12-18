import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

a = int(input())
Sum = 0
lastPrime = 3
for i in range(3, a + 1, 2):  # 只对奇数进行检测
    flag = isPrime(i)
    if flag:
        if i - lastPrime == 2:
            Sum += 1
        lastPrime = i
print(Sum)
