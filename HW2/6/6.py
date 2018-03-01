"""Wien's displacement law"""
import math


def intensity(x_min,x_max,T):

	while(True):
		root1=derivative(x_min,T)
		root2=derivative(x_max,T)
		mid=(x_min+x_max)/2
		root3=derivative(mid,T)
		if root1*root2 >= 0:
			print("Give a different initial range of roots")
			exit(0)
		else:
			if root1*root3 < 0:
				x_max=mid
			else:
				x_min=mid
		if abs(x_max - x_min) < 10e-8:
			break

	return mid


def derivative(l,T):
	a = 3.74e-16
	b = 0.0144/T
	c = math.exp(b/l)
	dI=(a*pow(l,-6)*(b*c/l - 5*(c - 1)))/((c - 1)**2)
	return dI

T=input("Enter the Temp:")
T=float(T)
x_min=1e-10
x_max=10e3
root=intensity(x_min,x_max,T)
wdc=root*T
print("Weins's constant:" %(wdc))