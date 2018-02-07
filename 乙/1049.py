N = int(input())
nums = list(map(float, input().split()))
Sum = 0
for i in range(0, N):
    Sum += (i + 1) * (N - i) * nums[i]   # 找规律
print("%.2f" % (Sum))
