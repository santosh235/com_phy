"""Quadratic equations."""
import math


def method_1(a, b, c):
    D = math.sqrt((b * b) - (4 * a * c))
    x1 = (D - b) / (2 * a)
    x2 = (D + b) / (2 * a)
    x2 = -x2
    print("The roots of the equations are: %f " % x1)
    print("The roots of the equations are: %f " % x2)
    return 0


def method_2(a, b, c):
    D = math.sqrt((b * b) - (4 * a * c))
    x1 = (2 * c) / (D + b)
    x1 = -x1
    x2 = (2 * c) / (D - b)
    print("The roots of the equations are: %f " % x1)
    print("The roots of the equations are: %f " % x2)
    return 0


print("Answer to part A:")
a = input("Enter a :")
b = input("Enter b:")
c = input("Enter c:")
a = float(a)
b = float(b)
c = float(c)

print("Answer to part A:")
method_1(a, b, c)

print("Answer to part B:")
method_2(a, b, c)
