def judge(str1):
    flag1 = 0
    flag2 = 1
    la = 0   #P左边的A数量
    ma = 0   #PT中间的A数量
    ra = 0   #T右边的A数量
    for x in str1:
        if flag1 == 0:
            if x == "A":
                la += 1
            elif x == "P":     #读到第一个P进入下一个状态
                flag1 = 1
                continue
            else:
                flag2 = 0
                break
        if flag1 == 1:
            if x == "A":
                ma += 1
            elif x == "T":    #读到第一个T进入下一个状态
                flag1 = 2
                continue
            else:
                flag2 = 0
                break
        if flag1 == 2:
            if x == "A":
                ra += 1
            else:
                flag2 = 0
                break
    if flag2 == 0 or flag1 != 2:     #若没有进入最终状态或没有满足前置条件则退出
        print("NO")
        return
    if la == 0 and ra == 0 and ma != 0:       #考虑前后没有A的情况
        print("YES")
        return
    if la != 0 and ma != 0 and ra / la == ma:    #若前后均有A，则必须满足此条件
        print("YES")
        return
    print("NO")
    return


a = int(input())
for i in range(0, a):
    str2 = input()
    judge(str2)
