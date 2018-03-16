N, M = map(int, input().split())
for i in range(N):
    result1 = list(map(int, input().split()))
    result2 = result1[1:]
    for j in range(1, len(result1)):
        if result1[j] < 0 or result1[j] > M:
            result2.remove(result1[j])
    result2.remove(max(result2))
    result2.remove(min(result2))
    avarage = (sum(result2) / len(result2) + result1[0]) / 2
    if int(avarage) + 1 - avarage > avarage - int(avarage):
        print(int(avarage))
    else:
        print(int(avarage) + 1)
