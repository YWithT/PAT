N, M = map(int, input().split())
value = list(map(int, input().split()))
answer = input().split()
for i in range(0, N):
    Sum = 0
    student = input().split()
    for j in range(0, M):
        if student[j] == answer[j]:
            Sum += value[j]
    print(Sum)