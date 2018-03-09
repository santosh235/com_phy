from math import sin
from math import sqrt

def f(x):
    return sin(sqrt(100*x))**2

s=0.0
a=0.0
b=1.0
N=1
h=(b-a)/N

s=0.5*f(a)+0.5*f(b)
I=h*s
I_last = 0  # just an initialization value
I1=round(I,6)
for N in range(1,40,2):
    h=(b-a)/N
    s=0.5*f(a)+0.5*f(b)
    for k in range(1,N):
        
        s+=f(a+k*h)
        I=h*s
        I1=round(I,6)
    print("deviation = ", (I - I_last)/3)
    I_last = I
        
    print("N =", N)
    #print("error = ", (1/3)*(I2-I1))
    #print(resultat)
    print("I=",I1)


