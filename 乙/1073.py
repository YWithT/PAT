N, M = map(int, input().split())
questions = []
error_list = [0] * M
value_list = []
answer_list = []
for i in range(0, M):
    string = input().split()
    value_list.append(int(string[0]))
    answer_list.append(string[2:])

for i in range(0, N):
    string = input()
    gradeSum = 0
    string = string[1:-1].split(') (')
    for j in range(0, M):
        answer = ' '.join(answer_list[j])
        if answer == string[j]:
            gradeSum += value_list[j]
        else:
            error_list[j] += 1
    print(gradeSum)

max_value = max(error_list)
if max_value == 0:
    print("Too simple")
else:
    print(max_value, end='')
    for i in range(M):
        if error_list[i] == max_value:
            print(' ' + str(i + 1), end="")
