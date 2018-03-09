# Adaptive trapezoidal rule and Romberg integral
from math import sin
from math import sqrt
N = 0

def f(x):
    return sin(sqrt(100*x))**2


def trapezoidal(a,b):
    h = abs((b-a)/2)
    z = 0

    for i in range(1,2):
        z = z + f(a + i*h)

    result = ((f(a)+f(b)+2*z)*h)/2
    return result



def recursive_asr(a,b,eps,whole):
    c = (a+b) / 2.0
    left = trapezoidal(a,c)
    right = trapezoidal(c,b)
    global N 
    if abs(left + right - whole) <= eps:
        return left + right
    
    print("Interation for ad_trap_rule N = %d " %(N))
    N = N + 1
    return recursive_asr(a,c,eps/2.0,left) + recursive_asr(c,b,eps/2.0,right)

def adaptive_trapezoidal_rule(a,b,eps):
    return recursive_asr(a,b,eps,trapezoidal(a,b))

print (" The integral value  after adaptive_trapezoidal rule is :%f " %(adaptive_trapezoidal_rule(0,1,1e-6)))


