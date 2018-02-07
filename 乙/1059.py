import math


def isPrime(x):
    if x == 1 or x == 0:
        return False
    else:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
    return True


N = int(input())
players = []
searchedPlayers = []
for i in range(0, N):
    players.append(input())
M = int(input())
for i in range(0, M):
    searchId = input()
    if searchId in searchedPlayers:
        print("%s: Checked" % searchId)
    elif searchId not in players:
        print("%s: Are you kidding?" % searchId)
    else:
        rank = players.index(searchId) + 1
        searchedPlayers.append(searchId)
        if rank == 1:
            print("%s: Mystery Award" % searchId)
        elif isPrime(rank):
            print("%s: Minion" % searchId)
        else:
            print("%s: Chocolate" % searchId)

