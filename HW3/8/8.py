"""Adaptive Simpson's rule"""
from math import sin
from math import sqrt
N = 0

def f(x):
    return sin(sqrt(100*x))**2


def simpson(a,b):
    c = (a+b) / 2.000
    h3 = abs(b-a) / 6.0
    return h3*(f(a) + 4.0*f(c) + f(b))


def recursive_asr(a,b,eps,whole):
    "Recursive implementation of adaptive Simpson's rule."
    c = (a+b) / 2.0
    left = simpson(a,c)
    right = simpson(c,b)
    global N 
    if abs(left + right - whole) <= eps:
        return left + right
    
    print("Iteration for ad_simp_rule N = %d " %(N))
    N = N + 1
    return recursive_asr(a,c,eps/2.0,left) + recursive_asr(c,b,eps/2.0,right)

def adaptive_simpson_rule(a,b,eps):
    return recursive_asr(a,b,eps,simpson(a,b))

print (" The integral value  after adaptive_simp rule is :%f " %(adaptive_simpson_rule(0,1,1e-6)))


