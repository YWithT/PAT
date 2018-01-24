def insertion_sort(numList1, numList2):
    flag = 0
    for i in range(1, len(numList1)):
        for j in range(i, 0, -1):
            if numList1[j] < numList1[j - 1]:
                media = numList1[j]
                numList1[j] = numList1[j - 1]
                numList1[j - 1] = media
            else:
                break
        if flag == 1:
            print("Insertion Sort")
            str1 = ""
            for num in numList1:
                str1 += str(num) + " "
            print(str1.strip())
            return
        if numList1 == numList2:
            flag = 1

# 只是用排序的思想解题，并非真正的排序算法
def merge_sort(numList1, numList2):
    i = 2
    flag = 0
    while (i < len(numList1) * 2):
        for j in range(0, len(numList1), i):
            if j + i > len(numList1):
                a_sort = sorted(numList1[j:len(numList1)])
                numList1[j:len(numList1)] = a_sort
            else:
                a_sort = sorted(numList1[j:j + i])
                numList1[j:j + i] = a_sort
        if flag == 1:
            print("Merge Sort")
            str1 = ""
            for num in numList1:
                str1 += str(num) + " "
            print(str1.strip())
            return
        if numList1 == numList2:
            flag = 1
        i *= 2


N = int(input())
numlist1 = list(map(int, input().split()))
numlist2 = list(map(int, input().split()))
numlist11 = numlist1[:]
numlist22 = numlist2[:]
insertion_sort(numlist1, numlist2)
merge_sort(numlist11, numlist22)
