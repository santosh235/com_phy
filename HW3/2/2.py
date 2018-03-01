"Simpson's Rule Vs Trapezoidal Rule"

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

def trapezoidal(a,b,slices):
	h = (b-a)/slices
	z = 0

	for i in range(1,slices):
		z = z + f(a + i*h)

	result = ((f(a)+f(b)+2*z)*h)/2
	return result

def err(orig,approx):
	err = (abs(orig - approx)/orig)
	return err


simp_10 	= 	simpson(0,2,10)
simp_100 	=	simpson(0,2,100)
simp_1000	=	simpson(0,2,1000)

trap_10 	= 	trapezoidal(0,2,10)
trap_100 	= 	trapezoidal(0,2,1000)
trap_1000 	= 	trapezoidal(0,2,1000)

print("Simpson' rule:The result with 10 slices is :%f and the corresponding error is :%f" %(simp_10,err(4.4,simp_10)))

print("Simpson' rule:The result with 100 slices is :%f and the corresponding error is :%f" %(simp_100,err(4.4,simp_100)))

print("Simpson' rule:The result with 1000 slices is :%f and the corresponding error is :%f" %(simp_1000,err(4.4,simp_1000)))

print("Trapezoidal's rule:The result with 10 slices is :%f and the corresponding error is :%f" %(trap_10,err(4.4,trap_10)))

print("Trapezoidal's rule:The result with 100 slices is :%f and the corresponding error is :%f" %(trap_100,err(4.4,trap_100)))
print("Trapezoidal's rule:The result with 1000 slices is :%f and the corresponding error is :%f" %(trap_1000,err(4.4,trap_1000)))
