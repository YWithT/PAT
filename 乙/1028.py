N = input()
Sum = 0
MaxTime = now = "2014/09/06"
MinTime = before = "1814/09/06"
for i in range(0, int(N)):
    x = raw_input().split()
    if before <= x[1] <= now:
        Sum += 1
        if x[1] < MaxTime:
            Max = x[0]
            MaxTime = x[1]
        if x[1] > MinTime:
            Min = x[0]
            MinTime = x[1]
if N == "0":
    print(0)
else:
    print("%d %s %s" % (Sum, Max, Min))
