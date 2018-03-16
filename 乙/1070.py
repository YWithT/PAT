N = int(input())
nums = list(map(int, input().split()))
nums.sort()
for i in range(len(nums)):
    if i == 0:
        Sum = nums[i]
    else:
        Sum = (Sum + nums[i]) / 2.0
print(int(Sum))