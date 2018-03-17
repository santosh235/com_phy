# -*- coding: utf-8 -*-
# @Author: santosh
# @Date:   2018-03-15 23:54:49
# @Last Modified by:   santosh


""" Integration using Monte-Carlo and mean value method"""

import numpy as np 
import math
import random

#function definition
def f(x):
	den = x * (2 - x)
	z = (math.sin(1/den) ** 2)
	return z



#MONTE-CARLO METHOD

# define any xmin-xmax interval here! (xmin < xmax)
xmin = 0.0
xmax = 2.0

# find ymin-ymax
numSteps = 10000
ymin = 0.0
ymax = ymin
for i in range(1,numSteps):
    x = xmin + (xmax - xmin) * float(i) / numSteps
    y = f(x)
    if y < ymin: ymin = y
    if y > ymax: ymax = y



rectArea = (xmax - xmin) * (ymax - ymin)        #Area of rectangular region
numPoints = 10000                           #Number of points for Monte-carlo sims
ctr = 0                                     #Number of points lying with the curve intialized to zero

for j in range(numPoints):
    x = xmin + (xmax - xmin) * random.random()
    y = ymin + (ymax - ymin) * random.random()
    if math.fabs(y) <= math.fabs(f(x)):
    	if f(x) > 0 and y > 0 and y <= f(x):
    		ctr += 1 # area over x-axis is positive
    	if f(x) < 0 and y < 0 and y >= f(x):
        	ctr -= 1 # area under x-axis is negative

Integral = rectArea * float(ctr) / numPoints            # Integration calculation
print("Numerical integration (Hit-Miss Monte-carlo) = %f" %(Integral))


""" Mean -Value Method """

X = np.random.rand(numPoints) * 2       #Generating a set of random-points
F_tot = 0

for i in range(numPoints):
	F_X = f(X[i])
	F_tot = F_tot + F_X

I = (xmax - xmin) * F_tot / numPoints       # Integration calculation

print("Integral Value (Mean- Value Method) = %f" %(I))