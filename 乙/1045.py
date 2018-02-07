N = int(input())
nums1 = list(map(int, input().split()))
nums2 = sorted(nums1.copy())
result = []
Max = 0
for i in range(0, N):
    if Max < nums1[i]:
        Max = nums1[i]
    if nums1[i] == nums2[i] and nums1[i] == Max:
        result.append(nums2[i])
print(len(result))
for i in range(0, len(result)):
    if i != len(result) - 1:
        print(result[i], end=' ')
    else:
        print(result[i], end='')
print()
