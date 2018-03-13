# -*- coding: utf-8 -*-
# @Author: santosh
# @Date:   2018-03-11 23:38:15
# @Last Modified by:   santosh
# @Last Modified time: 2018-03-12 10:27:34


""" Integration using Monte-Carlo and mean value method"""

import numpy as np 
import math
import random


def f(x):
	den = x * (2 - x)
	z = (math.sin(1/den) ** 2)
	return z


N = 10000
k = 0
for i in range(N):
	x = np.random.uniform(0,2)
	y = np.random.uniform(0,1)

	if y <= f(x):
		k = k + 1
integral = k * 2 / N

print(integral)

# define any xmin-xmax interval here! (xmin < xmax)
xmin = 0.0
xmax = 2.0

# find ymin-ymax
numSteps = 1000000 # bigger the better but slower!
ymin = 0.0
ymax = ymin
for i in range(1,numSteps):
    x = xmin + (xmax - xmin) * float(i) / numSteps
    y = f(x)
    if y < ymin: ymin = y
    if y > ymax: ymax = y

# Monte Carlo
rectArea = (xmax - xmin) * (ymax - ymin)
numPoints = 10000 
ctr = 0
for j in range(numPoints):
    x = xmin + (xmax - xmin) * random.random()
    y = ymin + (ymax - ymin) * random.random()
    if math.fabs(y) <= math.fabs(f(x)):
    	if f(x) > 0 and y > 0 and y <= f(x):
    		ctr += 1 # area over x-axis is positive
    	if f(x) < 0 and y < 0 and y >= f(x):
        	ctr -= 1 # area under x-axis is negative

fnArea = rectArea * float(ctr) / numPoints
print("Numerical integration = %f" %(fnArea))


""" Mean -Value Method """

X = np.random.rand(numPoints) * 2
F_tot = 0

for i in range(numPoints):
	F_X = f(X[i])
	F_tot = F_tot + F_X

I = (xmax - xmin) * F_tot / numPoints
print("%f" %(I))