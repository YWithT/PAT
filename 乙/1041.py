N = int(input())
students = []
for i in range(0, N):
    student = list(input().split())
    students.append(student)
M = int(input())
seats = list(input().split())
for seat in seats:
    for student in students:
        if seat == student[1]:
            print(student[0] + " " + student[2])
            break
