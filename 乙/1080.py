P, M, N = map(int, input().split())
students = []
for i in range(P):
    stu, G1 = map(str, input().split())
    if int(G1) >= 200:
        student = [stu, int(G1)]
        students.append(student)

for i in range(M):
    stu, G2 = map(str, input().split())
    for student in students:
        if stu in student:
            student.append(int(G2))

for student in students:
    if len(student) <= 2:
        student.append(-1)
for i in range(N):
    stu, G3 = map(str, input().split())
    for student in students:
        if stu in student:
            student.append(int(G3))

students_New = students.copy()
for student in students:
    if student[2] > student[3] and student[2] * 0.4 + student[3] * 0.6 <= 60:
        students_New.remove(student)
    elif student[2] <= student[3] <= 60:
        students_New.remove(student)

for student in students_New:
    if student[2] < student[3]:
        student.append(student[3])
    else:
        student.append(int(student[2] * 0.4 + student[3] * 0.6 + 0.5))
students_New.sort(key=lambda l: (-l[4], l[0]), reverse=False)
for student in students_New:
    print(student[0] + " " + str(student[1]) + " " + str(student[2]) + " " + str(student[3]) + " " + str(student[4]))
