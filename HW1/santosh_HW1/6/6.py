#Planetary orbit
import math

G=6.67e-7
M=2.0e30

l1=input("Enter the distance to the sun:")
v1=input("Enter the perihilion velocity")
l1=float(l1)
v1=float(v1)
a_inverse=((2/l1)-(v1*v1)/(G*M))
a=1/a_inverse
l2=2*a-l1
v2=(l1*v1)/l2
T_sq=(4.0*3.14*3.14*(a**(3))/(G*M))
T=math.sqrt(T_sq)
x=l1/l2
e=(1-x)/(1+x)
print("The aphelion distance(in meters): %f" %l2)
print("The velocity at aphelion (in m/s):%f" %v2)
print("The eccentricity is : %f" %e)
print("The time period in second is :%f" %T)
