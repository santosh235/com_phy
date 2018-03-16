# -*- coding: utf-8 -*-
# @Author: santosh
# @Date:   2018-03-15 22:16:25
# @Last Modified by:   santosh
# @Last Modified time: 2018-03-15 22:58:01


""" The dimer covering problem"""

import numpy as np 
import random
from math import exp
import matplotlib.pyplot as plt


L = 50
N = 1000

# for i in range(N):
# 	x = random.randint(0,L)
# 	y = random.randint(0, L)
# 	z = random.randint(0,4)
# 	if z==0:
# 		x_adj = x + 1
# 		y_adj = y
# 	elif z==1:
# 		x_adj = x - 1
# 		y_adj = y
# 	elif z==1:
# 		x_adj = x
# 		y_adj = y + 1
# 	else:
# 		x_adj = x 
# 		y_adj = y - 1

# 	if x_adj >= L || x_adj < 0 || y_adj >= L || y_adj < 0:
# 		i = i - 1
# 		continue

x = np.linspace(0,L,50)
y = np.linspace(0,L,50)

y[5] = 1
# padded_config = [[0 for x in range(L)] for y in range(L)]
# plt.plot(x,y,padded_config)
plt.plot(x,y)
print(x)

# plt.grid()


plt.show()