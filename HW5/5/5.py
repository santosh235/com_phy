# -*- coding: utf-8 -*-
# @Author: santosh
# @Date:   2018-03-12 17:53:25
# @Last Modified by:   santosh
# @Last Modified time: 2018-03-15 11:16:49


""" Volume of a Hyper-Sphere"""

import numpy as np 

D = input("Enter the dimension:")
D = int(D)

N = 1000000
count = 0
x = np.zeros(D)

for i in range(N):
	k = 0
	for j in range(D):
		x[j] = np.random.uniform(-1,1)
		k = k + x[j] * x[j]
	if k <= 1:
		count += 1

volume = (2 ** D) * (count) / N

print("Volume  : %f" %(volume))