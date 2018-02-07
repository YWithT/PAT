N = int(input())
nums = input().split()
result = []
for num in nums:
    Sum = 0
    for x in num:
        Sum += int(x)
    if Sum not in result:
        result.append(Sum)
result.sort()
print(len(result))
result = map(str, result)
print(" ".join(result))
