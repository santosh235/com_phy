# -*- coding: utf-8 -*-
# @Author: santosh
# @Date:   2018-03-11 23:38:15
# @Last Modified by:   santosh
# @Last Modified time: 2018-03-11 23:46:20


""" Integration using Monte-Carlo and mean value method"""

import numpy as np 
import matplotlib.pyplot as plt 
from math import sin



def f(x):
	den = x * (2 - x)
	z = (sin(1/den) ** 2)
	return z


N = 10000000000
k = 0
for i in range(N):
	x = np.random.uniform(0,2)
	y = np.random.uniform(0,1)

	if y <= f(x):
		k = k + 1
integral = k * 2 / N

print(integral)