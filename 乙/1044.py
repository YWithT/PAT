lows = ["tret", "jan", "feb", "mar", "apr", "may", "jun", "jly", "aug", "sep", "oct", "nov", "dec"]
highs = ["tret", "tam", "hel", "maa", "huh", "tou", "kes", "hei", "elo", "syy", "lok", "mer", "jou"]
N = int(input())
for i in range(0, N):
    string = input()
    if '0' <= string[0] <= '9':
        num = int(string)
        if num < 13:
            print(lows[num])
        else:
            low = num % 13
            high = num // 13
            if low != 0:
                print(highs[high] + " " + lows[low])
            else:
                print(highs[high])
    else:
        words = string.split()
        if len(words) == 2:
            num = highs.index(words[0]) * 13 + lows.index(words[1])
        else:
            if words[0] in lows:
                num = lows.index(words[0])
            elif words[0] in highs:
                num = highs.index(words[0]) * 13
        print(num)
