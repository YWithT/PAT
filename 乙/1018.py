def judge(char1, char2):
    if char1 == "C" and char2 == "J":
        return 1
    elif char1 == "C" and char2 == "B":
        return 2
    elif char1 == "C" and char2 == "C":
        return 0
    elif char1 == "B" and char2 == "C":
        return 1
    elif char1 == "B" and char2 == "B":
        return 0
    elif char1 == "B" and char2 == "J":
        return 2
    elif char1 == "J" and char2 == "C":
        return 2
    elif char1 == "J" and char2 == "B":
        return 1
    elif char1 == "J" and char2 == "J":
        return 0


n = int(input())
player1 = [0, 0, 0]
player1win = [["C", 0], ["B", 0], ["J", 0]]
player2win = [["C", 0], ["B", 0], ["J", 0]]
for i in range(0, n):
    a = input().split()
    a0 = a[0]
    a1 = a[1]
    x = judge(a0, a1)
    if x == 1:
        player1[0] += 1
        if a0 == "C":
            player1win[0][1] += 1
        elif a0 == "B":
            player1win[1][1] += 1
        else:
            player1win[2][1] += 1
    elif x == 0:
        player1[1] += 1
    else:
        player1[2] += 1
        if a1 == "C":
            player2win[0][1] += 1
        elif a1 == "B":
            player2win[1][1] += 1
        else:
            player2win[2][1] += 1
player1win.sort(key=lambda x: (-x[1], x[0]))
player2win.sort(key=lambda x: (-x[1], x[0]))
print("%d %d %d" % (player1[0], player1[1], player1[2]))
print("%d %d %d" % (player1[2], player1[1], player1[0]))
print("%c %c" % (player1win[0][0], player2win[0][0]))
