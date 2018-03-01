"""Nonlinear equation"""

import math

def f(x,y):
	f = pow(y,2)*(1-x)-pow(x,3)
	return f


def g(x,y):
	g = pow(y,2) + pow(x,2) - 1
	return g

def f_prime_x(x,y):
	f_prime = -pow(y,2) - 3*pow(x,2)
	return f_prime

def f_prime_y(x,y):
	f_prime = 2*y*(1-x)
	return f_prime

def g_prime_x(x,y):
	g_prime = 2*x
	return g_prime

def g_prime_y(x,y):
	g_prime = 2*y
	return g_prime

def root_x(x,y):
	x_new = x + (f_prime_y(x,y)*g(x,y) - g_prime_y(x,y)*f(x,y))/(f_prime_x(x,y)*g_prime_y(x,y) - f_prime_y(x,y)*g_prime_x(x,y))
	return x_new

def root_y(x,y):
	y_new = y + (g_prime_x(x,y)*f(x,y) - f_prime_x(x,y)*g(x,y))/(f_prime_x(x,y)*g_prime_y(x,y) - f_prime_y(x,y)*g_prime_x(x,y))
	return y_new

def result_x(x,y):
	x_new = root_x(x,y)
	while(True):
		if abs(x_new - x) < 1e-6:
			break
		else:
			x = x_new
			x_new = root_x(x,y)
	return x_new

def result_y(x,y):
	y_new = root_y(x,y)
	while(True):
		if abs(y_new - y) < 1e-3:
			break
		else:
			y = y_new
			y_new = root_y(x,y)
	return y_new	

x = input("Enter rough estimate of x:")
y = input("Enter rough estimate of y:")
x = float(x)
y = float(y)

print("x::%f" %(result_x(x,y)))
print("y::%f" %(result_y(x,y)))