x = int(input())
listVal = [0] * (x+1)
Max = 0
for i in range(0, x):
    a = input().split()
    index = int(a[0])
    grade = int(a[1])
    listVal[index] += grade
    if listVal[index] > Max:
        Max = listVal[index]
        MaxIndex = index
print("%d %d" % (MaxIndex, Max))
