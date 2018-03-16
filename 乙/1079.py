def judge(string):
    list1 = list(string)
    list2 = list1.copy()
    list2.reverse()
    if list2 == list1:
        return True
    else:
        return False


def reverse(string):
    list1 = list(string)
    list1.reverse()
    return "".join(list1)


num = input()
flag = 0
for i in range(10):
    if judge(num):
        print(num + " is a palindromic number.")
        flag = 1
        break
    else:
        result = str(int(num) + int(reverse(num)))
        print(num + " + " + reverse(num) + " = " + result)
        num = result
if flag == 0:
    print("Not found in 10 iterations.")
