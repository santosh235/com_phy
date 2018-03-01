"""4.The Diffraction limit of a telescope"""

import math
import matplotlib.pyplot as plt 


def f(x, m, theta):
	z = math.cos(m*theta - x*math.sin(theta))
	return z

def J_m_x(m, x):
	a = 0.0
	b = math.pi
	slices = 1000
	h = (b-a)/slices
	z_odd=0
	z_even=0

	for i in range(1,slices,2):
		z_odd = z_odd + f(x, m, a + i*h)

	for i in range(2,slices,2):
		z_even = z_even + f(x, m, a + i*h)

	result = ((f(x, m, a) + f(x, m, b) + 4*z_odd + 2*z_even)*h)/3
	return result

def J_m(m):
	i = 0
	x = []
	J_m = []

	while(True):
		x.append(i*0.1)
		ans = J_m_x(m,x[i])
		J_m.append(float(ans))
		print("FOR x = %f  J(x) = %f" %(x[i],J_m[i]))
		if x[i] == 20:
			break
		i = i+1
	return x,J_m

x = []
J_0_x = []
J_1_x = []
J_2_x = []

x,J_0_x = J_m(0)
x,J_1_x = J_m(1)
x,J_2_x = J_m(2)



plt.plot(x,J_0_x,label=r'$J_0$')
plt.plot(x,J_1_x,label=r'$J_1$')
plt.plot(x,J_2_x,label=r'$J_2$')

plt.xlabel(r'$x$')
plt.ylabel(r'$J_m(x)$')
plt.legend(fontsize=10)
plt.savefig('4_Difraction_limit.png', bbox_inches='tight')
plt.show()



