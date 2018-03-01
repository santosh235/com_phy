# Q3:TO PRINT POLAR COORDINATES
import math
import numpy as np
x=input("Enter the X-cordinate:")
y=input("\n Enter the Y-cordinate:")
x=float(x)
y=float(y)

r=x*x+y*y
r=math.sqrt(r)

rad=np.arctan(abs(y)/abs(x))
theta=(360*rad)/(2*3.14)

if x<0 and y>0 :
	theta=theta+90
if x<0 and y<0 :
	theta=theta+180
if x>0 and y<0 :
	theta=theta+270

print("R=%f" %r)
print("theta=%f" %theta)
