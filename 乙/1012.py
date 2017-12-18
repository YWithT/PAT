a = input()
a = a.split()
W1 = []
W2 = []
W3 = []
W4 = []
W5 = []
b = []
A = [0, 0, 0, 0, 0]
Af = [0, 0, 0, 0, 0]
for i in range(1, len(a)):
    b.append(int(a[i]))
for x in b:
    if x % 5 == 1:
        W2.append(x)
    elif x % 5 == 2:
        W3.append(x)
    elif x % 5 == 3:
        W4.append(x)
    elif x % 5 == 4:
        W5.append(x)
    elif x % 5 == 0:
        W1.append(x)

for x in W1:
    if x % 2 == 0:
        Af[0] = 1
        A[0] += x

for x in range(0, len(W2)):
    Af[1] = 1
    if x % 2 == 0:
        A[1] += W2[x]
    else:
        A[1] -= W2[x]

if len(W3) != 0:
    Af[2] = 1
    A[2] = len(W3)

if len(W4) != 0:
    Af[3] = 1
    A[3] = sum(W4) / len(W4)

if len(W5) != 0:
    Af[4] = 1
    A[4] = max(W5)

for i in range(0, 5):
    if Af[i] != 0:
        if i != 3 and i != 4:
            print(str(A[i]) + " ", end="")
        elif i == 3:
            print("%.1f " % (A[i]), end="")
        elif i == 4:
            print(str(A[i]), end="")
    elif i != 4:
        print("N" + " ", end="")
    else:
        print("N", end="")
