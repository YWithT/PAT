string = input()
countP = countA = countT = counte = counts = countt = 0
for i in string:
    if i == "P":
        countP += 1
    elif i == "A":
        countA += 1
    elif i == "T":
        countT += 1
    elif i == "e":
        counte += 1
    elif i == "s":
        counts += 1
    elif i == "t":
        countt += 1
while (countP != 0 or countA != 0 or countT != 0 or counte != 0 or counts != 0 or countt != 0):
    if countP != 0:
        print("P", end="")
        countP -= 1
    if countA != 0:
        print("A", end="")
        countA -= 1
    if countT != 0:
        print("T", end="")
        countT -= 1
    if counte != 0:
        print("e", end="")
        counte -= 1
    if counts != 0:
        print("s", end="")
        counts -= 1
    if countt != 0:
        print("t", end="")
        countt -= 1
