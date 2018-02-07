N, e, D = map(float, input().split())
mayEmpty = 0
empty = 0
for i in range(0, int(N)):
    electronicUse = list(map(float, input().split()))
    lowDays = 0
    for j in range(1, len(electronicUse)):
        if electronicUse[j] < e:
            lowDays += 1
    if electronicUse[0] / 2 < lowDays and electronicUse[0] <= D:
        mayEmpty += 1
    if electronicUse[0] / 2 < lowDays and electronicUse[0] > D:
        empty += 1

print('%.1f%% %.1f%%' % (mayEmpty / N * 100, empty / N * 100))
