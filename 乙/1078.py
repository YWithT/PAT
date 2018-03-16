type = input()
str1 = input()
i = 0
result = ""
if type == "C":
    while i < len(str1):
        j = i + 1
        con = 1
        while j < len(str1) and str1[j] == str1[i]:
            con += 1
            j += 1
        if con == 1:
            result = result + str1[i]
        else:
            result += str(con) + str1[i]
        i = j
if type == "D":
    while i < len(str1):
        if "0" <= str1[i] <= "9":
            for j in range(i, len(str1)):
                if "0" <= str1[j] <= "9":
                    continue
                else:
                    result += str1[j] * int(str1[i:j])
                    i = j
                    break
        else:
            result += str1[i]
        i += 1
print(result)
