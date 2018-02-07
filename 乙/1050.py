import math

N = int(input())
for i in range(1, int(math.sqrt(N + 1))):
    if N % i == 0:
        n = i
        m = int(N / n)
nums = sorted(list(map(str, input().split())), reverse=True)
if N == 1:  # 如果只有一个数，则直接输出
    print(num[0])
    exit()
matrix = [[0] * n for i in range(m)]
U, D, L, R = 0, m - 1, 0, n - 1  # 设置上下左右的边界
i = j = x = 0
while (x < N):
    while (j < R and x < N):
        matrix[i][j] = nums[x]
        j += 1
        x += 1
    while (i < D and x < N):
        matrix[i][j] = nums[x]
        i += 1
        x += 1
    while (j > L and x < N):
        matrix[i][j] = nums[x]
        j -= 1
        x += 1
    while (i > U and x < N):
        matrix[i][j] = nums[x]
        i -= 1
        x += 1
    U, D, L, R = U + 1, D - 1, L + 1, R - 1
    i += 1
    j += 1
    if x == N - 1:
        matrix[i][j] = nums[x]
        x += 1
for a in matrix:  # 输出矩阵
    print(" ".join(a))
