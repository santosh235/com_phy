"""Error Calculations"""

def f(x):
	z = x**4 -2*x + 1
	return z

def trapezoidal(a,b,slices):
	h = (b-a)/slices
	z = 0

	for i in range(1,slices):
		z = z + f(a + i*h)

	result = ((f(a)+f(b)+2*z)*h)/2
	return result

def err(I1,I2):
	er = abs((I1-I2)/3)
	return er



I1 = trapezoidal(0,2,10)
I2 = trapezoidal(0,2,20)

err = err(I1,I2)

print("The integral value with N = 10 is %f" %(I1))
print("The integral value with N = 20 is %f" %(I2))

print("The error is : %f" %(err))
