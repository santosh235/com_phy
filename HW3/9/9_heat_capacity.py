######################################################################
#
# Functions to calculate integration points and weights for Gaussian
# quadrature
#
# x,w = gaussxw(N) returns integration points x and integration
#           weights w such that sum_i w[i]*f(x[i]) is the Nth-order
#           Gaussian approximation to the integral int_{-1}^1 f(x) dx
# x,w = gaussxwab(N,a,b) returns integration points and weights
#           mapped to the interval [a,b], so that sum_i w[i]*f(x[i])
#           is the Nth-order Gaussian approximation to the integral
#           int_a^b f(x) dx
#
# This code finds the zeros of the nth Legendre polynomial using
# Newton's method, starting from the approximation given in Abramowitz
# and Stegun 22.16.6.  The Legendre polynomial itself is evaluated
# using the recurrence relation given in Abramowitz and Stegun
# 22.7.10.  The function has been checked against other sources for
# values of N up to 1000.  It is compatible with version 2 and version
# 3 of Python.
#
# Written by Mark Newman <mejn@umich.edu>, June 4, 2011
# You may use, share, or modify this file freely
#
######################################################################

from numpy import ones,copy,cos,tan,pi,linspace
import matplotlib.pyplot as plt
import math

def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w



def f(x):
    den = (math.exp(x) - 1)**2
    num = (x**4)*(math.exp(x))
    result = num/den
    return result

def Cv(T):
    theta_D = 428.0
    a = 0.0
    b = theta_D/T
    x,w = gaussxwab(50,a,b)
    l = len(x)
    integral = 0
    
    for i in range(0,l):
        integral = integral + w[i]*f(x[i])

    ans = (7725.24*integral)/(b**3)

    return ans

T = input("Enter the temp::")
T = float(T)
ans = Cv(T)
print("C_v : " +  str(ans))

Temp = linspace(5,500,100)
C_v = []
for i in range(0,100):
    C_v.append(float(Cv(Temp[i])))

plt.plot(Temp, C_v)
plt.xlabel('Temperature(T)')
plt.ylabel(r'$C_v$')
plt.savefig('Cv_vs_T_plot.png',bbox_inches = 'tight')
plt.show()
