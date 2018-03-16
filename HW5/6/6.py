# -*- coding: utf-8 -*-
# @Author: santosh
# @Date:   2018-03-14 19:43:15
# @Last Modified by:   santosh
# @Last Modified time: 2018-03-15 15:18:14


""" Importance Sampling """

import numpy as np 
from math import exp, sqrt
import random

def f(x):
	num = x ** (-0.5)
	den = exp(x) + 1.0
	return (num/den)

def w(x):
	return (x ** (-0.5))


I = 0
N= 1000000

for i in range(N):
	z = np.random.uniform(0,1)
	x = z ** 2
	I = I + f(x)/w(x)

I = 2 * (I/N)

print("Integral : %f"  %(I))
