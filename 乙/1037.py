def judge(G1, S1, K1, G2, S2, K2):
    if G1 > G2:
        return 1
    elif G1 < G2:
        return 2
    else:
        if S1 > S2:
            return 1
        elif S1 < S2:
            return 2
        else:
            if K1 > K2:
                return 1
            elif K1 < K2:
                return 2
            else:
                return 3


a = input().split()
G1, S1, K1 = map(int, a[0].split("."))
G2, S2, K2 = map(int, a[1].split("."))
flag = judge(G1, S1, K1, G2, S2, K2)
if flag == 2:
    if K2 >= K1:
        K3 = K2 - K1
    else:
        K3 = K2 + 29 - K1
        S2 -= 1
    if S2 >= S1:
        S3 = S2 - S1
    else:
        S3 = S2 + 17 - S1
        G2 -= 1
    G3 = G2 - G1
    print(str(G3) + "." + str(S3) + "." + str(K3))
elif flag == 1:
    if K1 >= K2:
        K3 = K1 - K2
    else:
        K3 = K1 - K2 + 29
        S1 -= 1
    if S1 >= S2:
        S3 = S1 - S2
    else:
        S3 = S1 - S2 + 17
        G1 -= 1
    G3 = G1 - G2
    print("-" + str(G3) + "." + str(S3) + "." + str(K3))
else:
    print("0.0.0")
