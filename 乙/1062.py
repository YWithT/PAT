def mgcd(x, y):
    if x < y:
        x, y = y, x
    d = x % y
    while d != 0:
        x = y
        y = d
        d = x % y
    if y != 1:
        return False
    else:
        return True


fraction1, fraction2, K = map(str, input().split())
numerator1, denominator1 = map(int, fraction1.split("/"))
numerator2, denominator2 = map(int, fraction2.split("/"))
K = int(K)
Max = max(eval(fraction1), eval(fraction2))
Min = min(eval(fraction1), eval(fraction2))
i = 1
result = []
while (i / K) < Max:
    if (i / K) > Min and mgcd(i, K):
        result.append(str(i) + "/" + str(K))
    i += 1
print(" ".join(result))
