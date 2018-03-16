N = int(input())
password = ""
for i in range(N):
    str1 = input()
    index = str1.index("T")
    answer = str1[index - 2]
    password += str(ord(answer) - ord("A") + 1)
print(password)
