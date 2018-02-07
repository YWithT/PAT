def return_Expression(stringA):
    expressions = []
    for i in range(0, len(stringA)):
        if stringA[i] == '[':
            for k in range(i + 1, len(stringA)):
                if stringA[k] == ']':
                    expressions.append(stringA[i + 1: k])
                    break

    return expressions

a = input()
b = input()
c = input()
N = int(input())

hands = return_Expression(a)
eyes = return_Expression(b)
mouths = return_Expression(c)
error = "Are you kidding me? @\/@"

for i in range(0, N):
    nums = list(map(int, input().split()))
    if nums[0] < 1 or nums[1] < 1 or nums[2] < 1 or nums[3] < 1 or nums[4] < 1 or len(nums) != 5 or nums[0] > len(
            hands) or nums[1] > len(eyes) or nums[2] > len(mouths) or nums[3] > len(eyes) or nums[4] > len(hands):
        print(error)
        continue
    print(hands[nums[0] - 1] + "(" + eyes[nums[1] - 1] + mouths[nums[2] - 1] + eyes[nums[3] - 1] + ")" + hands[
        nums[4] - 1])
