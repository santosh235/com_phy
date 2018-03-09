""" FOURIER FILTERING AND  SMOOTHING"""


import matplotlib.pyplot as plt
import numpy as np
from math import sin,pi,hypot 

#DEFINING THE INTENSITY TRANSMISSION FUNCTION
def q(u):
	alpha = pi/20.
	z = sin(alpha * u) **2
	return z

N = 400
u = []
w = 200

#CREATING AN ARRAY OF 4000 POINTS
for n in range(10 * N):
	if (n < N):
		p = (n * w / N) - (w / 2.)
		u.append(float(p))
	else :
		u.append(float(0))			#EXTRA POINTS ARE SET TO ZERO



# ARRAY OF Yn
y = []
for n in range(10 * N):
	y.append(float(q(u[n])))

#FOURIER TRANSFORMATION 
ck = np.fft.fft(y)

ck_sq =[]

# MOD SQUARE OF FOURIER COEFFIECIENTS
for i in range(len(ck)):
	ck_sq.append((ck[i] * ck[i].conjugate()))	

