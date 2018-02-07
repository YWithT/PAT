M, N, TOL = map(int, input().split())
matrix = []
result = []
value = []
deleteValue = []
directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
for i in range(N):
    nums = list(map(int, input().split()))
    matrix.append(nums)
for i in range(0, N):
    for j in range(0, M):
        try:
            for direction in directions:
                flag = 1
                if abs(matrix[i][j] - matrix[i + direction[0]][j + direction[1]]) <= TOL:
                    flag = 0
                    break
            if flag == 1:
                value.append(matrix[i][j])
        except:
            pass
for i in range(len(value)):
    if value.count(value[i]) != 1:
        deleteValue.append(value[i])
for i in range(len(value)):
    if value[i] not in deleteValue:
        result.append(value[i])

if len(result) == 1:
    for i in range(N):
        if result[0] in matrix[i]:
            j = matrix[i].index(result[0])
            print("(%d, %d): %d" % (j + 1, i + 1, matrix[i][j]))
elif len(result) > 1:
    print("Not Unique")
else:
    print("Not Exist")
