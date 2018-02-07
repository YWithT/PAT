N = int(input())
nums = input().split()
Count = 0
Sum = 0
for num in nums:
    try:
        #     x = float(num)
        #     if -1000 <= x <= 1000 and "." not in num:
        #         Sum += x
        #         Count += 1
        #     elif -1000 <= x <= 1000 and "." in num and len(num[num.index("."):]) <= 3:
        #         Sum += x
        #         Count += 1
        #     else:
        #         print("ERROR: %s is not a legal number" % num)
        # except:
        #     print("ERROR: %s is not a legal number" % num)
        if round(float(num), 2) == float(num) and -1000 <= float(num) <= 1000:
            Sum += float(num)
            Count += 1
        else:
            print("ERROR: %s is not a legal number" % num)
    except:
        print("ERROR: %s is not a legal number" % num)
if Count > 1:
    print("The average of %d numbers is %.2f" % (Count, Sum / Count))
elif Count == 1:
    print("The average of 1 number is %.2f" % Sum)
elif Count == 0:
    print("The average of 0 numbers is Undefined")
