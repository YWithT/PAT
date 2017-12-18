a = input().split()
A = a[0]
Da = a[1]
B = a[2]
Db = a[3]
Pa = ""
Pb = ""
for x in A:
    if x == Da:
        Pa += x
for x in B:
    if x == Db:
        Pb += x
if Pa != "":
    Pa = int(Pa)
else:
    Pa = 0
if Pb != "":
    Pb = int(Pb)
else:
    Pb = 0
print(Pa + Pb)
