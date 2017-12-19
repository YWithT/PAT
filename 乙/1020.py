N, D = list(map(int, input().split()))
Goods = list(map(float, input().split()))
Prices = list(map(float, input().split()))
rate = {i: Prices[i] / Goods[i] for i in range(N)}
order = sorted(rate, key=lambda i: rate[i], reverse=True)
Sum = 0

for i in order:
    if D >= Goods[i]:
        Sum += Prices[i]
        D -= Goods[i]
    else:
        Sum += D * rate[i]
        break

print('%.2f' % Sum)
