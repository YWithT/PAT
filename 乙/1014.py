A1 = input().strip()
A2 = input().strip()
A3 = input().strip()
A4 = input().strip()
flag = 1
for i in range(0, min(len(A1), len(A2))):
    if A1[i] == A2[i] and 'A' <= A1[i] <= 'G' and flag == 1:
        flag = 2
        Day = A1[i]
    elif A1[i] == A2[i] and flag == 2 and ('A' <= A1[i] <= 'N' or '0' <= A1[i] <= '9'):
        Hour = A1[i]
        break
for i in range(0, min(len(A3), len(A4))):
    if A3[i] == A4[i] and 'a' <= A3[i] <= 'z' or 'A' <= A3[i] <= 'Z':
        Min = i
        break

if Day == "A":
    Day = "MON"
elif Day == "B":
    Day = "TUE"
elif Day == "C":
    Day = "WED"
elif Day == "D":
    Day = "THU"
elif Day == "E":
    Day = "FRI"
elif Day == "F":
    Day = "SAT"
elif Day == "G":
    Day = "SUN"

if '0' <= Hour <= '9':
    Hour = int(Hour)
else:
    Hour = ord(Hour) - ord('A') + 10

print("%s %02d:%02d" % (Day, Hour, Min))
