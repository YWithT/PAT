wrongKey = input()
inputStr = input()
if "+" in wrongKey:
    for i in inputStr:
        if "A" <= i <= "Z":
            inputStr = inputStr.replace(i, "")
for i in wrongKey:
    if "A" <= i <= "Z":
        inputStr = inputStr.replace(i, "")
        inputStr = inputStr.replace(i.lower(), "")
    else:
        inputStr = inputStr.replace(i, "")

print(inputStr)
