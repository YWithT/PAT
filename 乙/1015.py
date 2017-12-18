a = input().split()
N = int(a[0])
L = int(a[1])
H = int(a[2])

Stu = []
one = []
two = []
three = []
four = []

for i in range(0, N):
    b = []
    a = input().split()
    b.append(int(a[0]))
    b.append(int(a[1]))
    b.append(int(a[2]))
    b.append(int(a[1]) + int(a[2]))
    Stu.append(b)

for i in Stu:
    if i[1] >= H and i[2] >= H:
        one.append(i)
    elif i[1] >= H and i[2] >= L:
        two.append(i)
    elif i[1] >= i[2] >= L:
        three.append(i)
    elif i[1] >= L and i[2] >= L:
        four.append(i)

print(len(one) + len(two) + len(three) + len(four))
one.sort(key=lambda student: student[3], reverse=True)


