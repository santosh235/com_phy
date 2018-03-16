# -*- coding: utf-8 -*-
# @Author: santosh
# @Date:   2018-03-15 23:55:00
# @Last Modified by:   santosh
# @Last Modified time: 2018-03-15 23:57:49

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

#Start point
x[0] = 50
y[0] = 50



# Million steps
i = 1
while (i != 1000000):
	val = random.randint(1,4)	#genearting a random number to choose the direction of motion

	#Given the value it generates the point moves accordingly
	# If the point  lies outside the lattice the movement is discarded withouting counting the step
	if val == 1 :
		if x[i -1] == 101:	
			continue
		else : 

			x[i] = x[i - 1] + 1		#
			y[i] = y[i - 1]
			i = i + 1		#Updating the count
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




#Data plotting
plt.title("Brownian motion")
plt.plot(x, y)
plt.xlim(0,101)
plt.ylim(0,101)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("brownian_motion.png",bbox_inches="tight")
plt.show()