string = input().lower()
words = []
letters = []
for x in string:
    if 'a' <= x <= 'z':
        if x not in letters:
            words.append([x, 1])
            letters.append(x)
        else:
            for word in words:
                if word[0] == x:
                    word[1] += 1
                    break
words = sorted(words, key=lambda word: (word[1], word[0]), reverse=True)
letter = words[0][0]
num = words[0][1]
for i in range(1, len(words)):
    if words[i][1] < num:
        break
    else:
        letter = words[i][0]
print(str(letter) + " " + str(num))
