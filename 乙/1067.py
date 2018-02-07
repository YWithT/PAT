string = input().split()
password = string[0]
tryTimes = int(string[1])
while tryTimes:
    string = input()
    if string == "#":
        exit()
    if string == password:
        print("Welcome in")
        exit()
    else:
        print("Wrong password: %s" % string)
    tryTimes -= 1
print("Account locked")
