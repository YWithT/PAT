M, N, S = map(int, input().split())
Winner = []
Names = []
for i in range(M):
    Names.append(input())
    if i >= S - 1 and (i - S + 1) % N == 0:
        if Names[i] in Winner:
            S += 1
        else:
            Winner.append(Names[i])
if len(Winner) != 0:
    for i in range(len(Winner)):
        print(Winner[i])
else:
    print("Keep going...")
