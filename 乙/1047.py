N = int(input())
teams = [0] * 1001
for i in range(0, N):
    a = input().split("-")
    b = a[1].split()
    team = int(a[0])
    grade = int(b[1])
    teams[team] += grade
print(str(teams.index(max(teams)))+" "+str(max(teams)))
