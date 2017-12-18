a = int(input())
result = []
for i in range(0, a):
    Nums = input()
    Nums = Nums.split()
    for j in range(0, len(Nums)):
        Nums[j] = int(Nums[j])
    if Nums[0] + Nums[1] > Nums[2]:
        result.append("true")
    else:
        result.append("false")
for i in range(0, len(result)):
    print("Case #"+str(i+1)+": "+result[i])
