a = input()
while (len(a) < 4):
    a = "0" + a
if a[0] == a[1] == a[2] == a[3]:
    print(a + " - " + a + " = " + "0000")
else:
    while 1:
        b = []
        b.append(a[0])
        b.append(a[1])
        b.append(a[2])
        b.append(a[3])
        b.sort()
        Min = int(b[0] + b[1] + b[2] + b[3])
        b.reverse()
        Max = int(b[0] + b[1] + b[2] + b[3])
        Sub = Max - Min
        print("%.4d - %.4d = %.4d" % (Max, Min, Sub))
        a = str(Sub)
        while (len(a) < 4):
            a = "0" + a
        if a == "6174":
            break
