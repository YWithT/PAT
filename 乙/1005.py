a = int(input())
Nums = input()
Nums = Nums.split()
for i in range(0, len(Nums)):
    Nums[i] = int(Nums[i])
Nums.sort(reverse=True)
Nums1 = list(Nums)
for i in range(0, len(Nums)):
    num = Nums[i]
    while (num != 1):
        if num % 2 == 0:
            num = num / 2
            if num in Nums1:
                Nums1.remove(num)
        else:
            num = num * 3 + 1
            if num in Nums1:
                Nums1.remove(num)

for i in range(0, len(Nums1)):
    print(str(Nums1[i]), end="")
    if i != len(Nums1) - 1:
        print(" ", end="")
