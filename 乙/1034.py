from fractions import Fraction


def minFormation(x):
    numerator = x._numerator.__abs__()
    denominator = x._denominator
    if denominator == 1:
        if x < 0:
            return "(" + str(x) + ")"
        else:
            return str(x)

    if numerator > denominator:
        integer = numerator // denominator
        remainder = numerator % denominator
        if x < 0:
            return "(-" + str(integer) + " " + str(remainder) + "/" + str(denominator) + ")"
        elif x > 0:
            return str(integer) + " " + str(remainder) + "/" + str(denominator)
    else:
        if x < 0:
            return "(-" + str(numerator) + "/" + str(denominator) + ")"
        elif x > 0:
            return str(numerator) + "/" + str(denominator)


a = input().split()
num1 = Fraction(a[0])
num2 = Fraction(a[1])
print(minFormation(num1) + " + " + minFormation(num2) + " = " + minFormation(num1 + num2))
print(minFormation(num1) + " - " + minFormation(num2) + " = " + minFormation(num1 - num2))
print(minFormation(num1) + " * " + minFormation(num2) + " = " + minFormation(num1 * num2))
if minFormation(num2) == "0":
    print(minFormation(num1) + " / " + minFormation(num2) + " = " + "Inf")
else:
    print(minFormation(num1) + " / " + minFormation(num2) + " = " + minFormation(num1 / num2))
