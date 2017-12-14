a = int(input())
b = []
c = []
grades = []
for i in range(0, a):
    b.append(input())
for i in b:
    i = i.split()
    c.append(i)
    grades.append(int(i[2]))
for i in c:
    if int(i[2]) == max(grades):
        print(i[0] + ' ' + i[1])
for i in c:
    if int(i[2]) == min(grades):
        print(i[0] + ' ' + i[1])
