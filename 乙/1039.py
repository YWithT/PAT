host = input()
customer = input()
readList = []
hostLength = len(host)
customerLength = len(customer)
flag = 1
plus = 0
sub = 0
for x in customer:
    if x not in readList:
        readList.append(x)
        hostCount = host.count(x)
        customerCount = customer.count(x)
        if hostCount >= customerCount:
            plus += hostCount - customerCount
            hostLength -= hostCount
        else:
            sub += customerCount - hostCount
            hostLength -= hostCount
            flag = 0
if flag == 1:
    print("Yes " + str(plus + hostLength))
else:
    print("No "+str(sub))
