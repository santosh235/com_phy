# Gamma Functions

from numpy import ones,copy,cos,tan,pi,linspace
import matplotlib.pyplot as plt
import math

def f(x,a):
	result = (x**(a - 1))*math.exp(-x)
	return result

x = linspace(0,5,100)
F_a_2 = []
F_a_3 = []
F_a_4 = []



for i in range(0,100):
	F_a_2.append(float(f(x[i],2)))
	F_a_3.append(float(f(x[i],3)))
	F_a_4.append(float(f(x[i],4)))

plt.plot(x,F_a_2,label = 'a=2')
plt.plot(x,F_a_3,label = 'a=3')
plt.plot(x,F_a_4,label = 'a=4')
plt.xlabel('x')
plt.ylabel('integrand')
plt.legend()
plt.savefig('integrand.png')