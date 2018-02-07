nums = list(map(int, input().split()))
Sum = 0
for i in range(1, len(nums)):
    for j in range(1, len(nums)):
        if i != j:
            Sum += int(str(nums[i]) + str(nums[j]))
print(Sum)
