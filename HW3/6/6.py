"""Error Calculations_simpson rule"""

def f(x):
	z = x**4 -2*x + 1
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

def err(I1,I2):
	er = abs((I1-I2)/15)
	return er



I1 = simpson(0,2,10)
I2 = simpson(0,2,20)

err = err(I1,I2)

print("The integral value with N = 10 is %f" %(I1))
print("The integral value with N = 20 is %f" %(I2))

print("The error is : %f" %(err))
