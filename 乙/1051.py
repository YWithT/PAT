import math

a = list(map(float, input().split()))
num1 = complex(a[0] * math.cos(a[1]), a[0] * math.sin(a[1]))
num2 = complex(a[2] * math.cos(a[3]), a[2] * math.sin(a[3]))
num3 = num1 * num2
real = num3.real
imag = num3.imag
if float(real) + 0.005 >= 0 and float(real) < 0:
    real = 0
if float(imag) + 0.005 >= 0 and float(imag) < 0:
    imag = 0
real = '%.2f' % real
imag = '%.2f' % imag
if imag > '0':
    print(str(real) + "+" + str(imag) + "i")
elif imag <= '0':
    print(str(real) + str(imag) + "i")
