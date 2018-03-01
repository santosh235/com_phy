""" Differentiaiting by integration"""
import cmath
from math import factorial,pi

def f(z):
	f_z = cmath.exp(2*z)
	return f_z

def argum(k):
	ar = cmath.exp(2 * pi * k * 1j/ 10000)
	return ar



z = []
N = 10000
for k in range(0,N+1):
	z.append(argum(k))

for m in range(1,21):
	der = 0
	for k in range(0,N):
		der = f(z[k]) * cmath.exp(-2 * pi * k * m * 1j/ 10000) + der
	der = der * factorial(m)/N
	mod, theta = cmath.polar(der)
	print(" Deriavtive no_%d is  :%.0f"  %(m,mod))

