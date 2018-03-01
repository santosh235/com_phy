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


def f(a,x):
    num = math.sqrt(8)
    den = math.sqrt(V(a) - V(x))
    return (num/den)


def V(x):
    V = (x**4)
    return V

def Time_pd(a):
    x,w = gaussxwab(20, 0, a)

    integral = 0
    for i in range(0,20):
        integral = integral + w[i]*f(a,x[i])

    return integral



a = input("Enter the amplitude:")
a = float(a)

T_pd = Time_pd(a)
print("The time period of oscillation for amplitude %f is %f" %(a, T_pd))

amp = linspace(0.1,2,200)
period = []

for i in range(0,200):
    period.append(float(Time_pd(amp[i])))

plt.plot(amp,period)
plt.xlabel('amplitude (a)')
plt.ylabel('Time period(T)')
plt.savefig("Timepd_plot.png", bbox_inches = 'tight')
plt.show()
