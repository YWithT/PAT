N, M = map(int, input().split())
B = input().split()
result = []
Sum = 0
for i in range(N):
    C = input().split()
    cache = []
    for j in range(2, 2 + int(C[1])):
        if C[j] in B:
            cache.append(C[j])
    if len(cache) != 0:
        Sum += len(cache)
        result.append(C[0])
        result.append(cache)
if len(result) != 0:
    for i in range(0, len(result), 2):
        print(result[i] + ":", end=" ")
        print(" ".join(result[i + 1]))
    print("%d %d" % (len(result) / 2, Sum))
else:
    print("0 0")
