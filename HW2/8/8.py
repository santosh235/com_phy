"""The roots of polynomial"""
from pylab import *
import math


def polynomial(x):
    p = 924*pow(x,6) - 2772*pow(x,5) + 3150*pow(x,4) -1680*pow(x,3) + 420*pow(x,2) - 42*x + 1
    return p

def derivative(x):
	p = 5544*pow(x,5) - 13860*pow(x,4) +12600*pow(x,3) - 5040*pow(x,2) + 840*x -42
	return p

def root(x_old):
	x_new=x_old - (polynomial(x_old)/derivative(x_old))
	
	while(True):
		if abs(x_new - x_old) < 10e-9:
			break
		else:
			x_old = x_new
			x_new=x_old - (polynomial(x_old)/derivative(x_old))

	return x_new



x = arange(0, 1.0001, 0.0001)
y = polynomial(x)

plot(x,y)
xlabel('x')
ylabel('P(x)')
savefig("8_polynomial.png")

print("Rough value of root after inspection:")
r1=0.04
r2=0.175
r3=0.38
r4=0.62
r5=0.84
r6=0.97
print(" a:: %.2f\n b:: %.2f\n c:: %.2f\n d:: %.2f\n e:: %.2f\n f:: %.2f" %(r1,r2,r3,r4,r5,r6))

print("The roots using Newton's method are:")
print(" a:: %f\n b:: %f\n c:: %f\n d:: %f\n e:: %f\n f:: %f" %(root(r1),root(r2),root(r3),root(r4),root(r5),root(r6)))