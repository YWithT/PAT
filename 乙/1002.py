str1 = input()
str2 = ""
b = []
for x in str1:
    b.append(int(x))
Sum = str(sum(b))
for x in Sum:
    if x == '1':
        str2 += "yi "
    elif x == "2":
        str2 += "er "
    elif x == "3":
        str2 += "san "
    elif x == "4":
        str2 += "si "
    elif x == "5":
        str2 += "wu "
    elif x == "6":
        str2 += "liu "
    elif x == "7":
        str2 += "qi "
    elif x == "8":
        str2 += "ba "
    elif x == "9":
        str2 += "jiu "
    elif x == "0":
        str2 += "ling "
print(str2.strip())
