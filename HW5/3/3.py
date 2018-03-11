# -*- coding: utf-8 -*-
# @Author: santosh
# @Date:   2018-03-11 18:00:28
# @Last Modified by:   santosh
# @Last Modified time: 2018-03-11 23:34:01


"""Brownian motion"""

import numpy
import matplotlib.pyplot as plt
import random
 
# defining the number of steps
L = 101
 
#creating two array for containing x and y coordinate
#of size equals to the number of size and filled up with 0's
x = numpy.zeros(1000000)
y = numpy.zeros(1000000)
x[0] = 50
y[0] = 50


# for i in range(1,100001):
# 	val = random.randint(1,4)

# 	if val == 1 :
# 		if x[i -1] == 101:
# 			i = i - 1
# 			continue
# 		else : 
# 			x[i] = x[i - 1] + 1
# 			y[i] = y[i - 1]

# 	elif val == 2:
# 		if x[i - 1] == 0:
# 			i = i - 1
# 			continue
# 		else:
# 			x[i] = x[i - 1] - 1
# 			y[i] = y[i - 1]
	
# 	elif val == 3:
# 		if y[i - 1] == 101:
# 			i = i - 1
# 			continue
# 		else:
# 			x[i] = x[i - 1]
# 			y[i] = y[i - 1] + 1
	
# 	else:
# 		if y[i - 1] == 0:
# 			i = i - 1
# 			continue
# 		else:
# 			x[i] = x[i -1]
# 			y[i] = y[i - 1] -1

i = 1
while (i != 1000000):
	val = random.randint(1,4)

	if val == 1 :
		if x[i -1] == 101:
			continue
		else : 

			x[i] = x[i - 1] + 1
			y[i] = y[i - 1]
			i = i + 1
	elif val == 2:
		if x[i - 1] == 0:
			continue
		else:

			x[i] = x[i - 1] - 1
			y[i] = y[i - 1]
			i = i + 1
	
	elif val == 3:
		if y[i - 1] == 101:
			continue
		else:

			x[i] = x[i - 1]
			y[i] = y[i - 1] + 1
			i = i + 1
	
	else:
		if y[i - 1] == 0:
			continue
		else:

			x[i] = x[i -1]
			y[i] = y[i - 1] -1
			i = i + 1





plt.title("Brownian motion")
plt.plot(x, y)
plt.xlim(0,101)
plt.ylim(0,101)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("brownian_motion.png",bbox_inches="tight")
plt.show()