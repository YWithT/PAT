parameters = list(map(int, input().split()))
N = parameters[0]
M = parameters[1]
Min = parameters[2]
Max = parameters[3]
replaceValue = parameters[4]
results = []
for i in range(N):
    nums = list(map(int, input().split()))
    for j in range(M):
        if Min <= nums[j] <= Max:
            nums[j] = replaceValue
    results.extend(nums)
for i in range(len(results)):
    results[i] = '%03d' % results[i]
for i in range(N):
    print(" ".join(results[i * M:(i + 1) * M]))
