a = input()
a = a.split()
string = ""
for i in range(0, len(a)):
    a[i] = int(a[i])
for i in range(0, len(a), 2):
    coe = a[i]
    index = a[i + 1]
    if index != 0:
        a[i] = coe * index
        a[i + 1] = index - 1
    elif index == 0:
        a[i] = 0
for i in range(0, len(a), 2):
    if a[i] != 0:
        string = string + str(a[i]) + " " + str(a[i + 1]) + " "
if string != "": 
    print(string.strip())   #��Ϊ�����ʽʱ�������
else:
    print("0 0")    #��Ϊ�����ʽʱ�����0 0��
