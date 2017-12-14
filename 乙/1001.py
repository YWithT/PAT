a = int(input())
step = 0
while (a != 1):
    if a % 2 == 0:
        a = a / 2
        step += 1
    else:
        a = (3 * a + 1) / 2
        step += 1
print(step)
