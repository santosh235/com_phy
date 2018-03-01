"""3 Integral"""

import math
import matplotlib.pyplot as plt 


def f(t):
	z = math.exp(-(t**2))
	return z


def simpson(a,b,slices):
	h = (b-a)/slices
	z_odd=0
	z_even=0

	for i in range(1,slices,2):
		z_odd = z_odd + f(a + i*h)

	for i in range(2,slices,2):
		z_even = z_even + f(a + i*h)

	result = ((f(a) + f(b) + 4*z_odd + 2*z_even)*h)/3
	return result






i = 0
x = []
E_x = []

while(True):
	x.append(float(i*0.1))
	ans = simpson(0,x[i],100)
	E_x.append(float(ans))
	print("FOR x = %f  E(x) = %f" %(x[i],E_x[i]))
	if x[i] == 3:
		break
	i = i+1


plt.plot(x,E_x,label='Plot of E(x)')
plt.xlabel('x')
plt.ylabel('E(x)')
plt.legend(fontsize=10)
plt.savefig('3_Integral_plot.png', bbox_inches='tight')