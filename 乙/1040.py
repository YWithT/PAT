stringOne = input()
Sum = 0
countT = stringOne.count("T")
countP = 0
for i in range(0, len(stringOne)):
    if stringOne[i] == "T":
        countT -= 1
    elif stringOne[i] == "P":
        countP += 1
    else:
        Sum += (countP * countT)
print(Sum % 1000000007)
