"""Factorial."""
import numpy as np

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = input("Enter the value of n:")
n_int = np.int(n)
n_float = np.float(n)

ans_1 = factorial(n_int)
ans_2 = factorial(n_float)

print("The answer as integer variable is : %d" % ans_1)
print("The answer as float variable is   : %d" % ans_2)
