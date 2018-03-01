"""Lagrange point"""
from pylab import *
import math

def lag_eq(r):
	M = 5.974e24
	m = 7.348e22
	R = 3.844e8

	f_x = (M/pow(r,2))-(m/pow(R-r,2))+(M*r/pow(R,3))

	return f_x



def secant(r1,r2):
	r3 = (r1*lag_eq(r2)-r2*lag_eq(r1))/(lag_eq(r2)-lag_eq(r1))
	return r3

def distance(r1,r2):
	r3=secant(r1,r2)
	while (True):
		if abs(r3-r2) < 1e-6:
			break
		else:
			r1=r2
			r2=r3
			r3=secant(r1,r2)
	return r3

r1 = 2.8e8
r2 = 3.2e8 

print("The distance of Lagrange point from earth is : %f" %(abs(distance(r1,r2))))