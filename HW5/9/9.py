# -*- coding: utf-8 -*-
# @Author: santosh
# @Date:   2018-03-15 22:16:25
# @Last Modified by:   santosh


""" The dimer covering problem"""

import numpy as np 
import random
from math import exp
import matplotlib.pyplot as plt


L = 50			#Size of the lattice
N = 200000		#No.of times to loop to run 
mat = np.empty((L, L))		#Creating an empty matrix of (L X L)
col = np.empty((2,2))
row = np.empty((2,2))


#Setting the plotting environment
fig = plt.figure()
ax = fig.gca()
ax.set_xticks(np.arange(-0.5, 50.5,1))			#grid spacing
ax.set_yticks(np.arange(-0.5, 50.5, 1))
plt.xlim(-0.5,49.5)
plt.ylim(-0.5,49.5)
plt.title(r'Dimer')
plt.xlabel(r'<-X->')
plt.ylabel(r'<-Y->')
plt.grid(color='r',linestyle='solid',linewidth=1)



# Choosing a two adjacent loation and placing a dimmer if empty
for i in range(N):
	x = random.randint(0, L-1)			#chossing a random site
	y = random.randint(0, L-1)			#chossing a random site
	z = random.randint(0,4)				#Choosing a random direction
	if z==0:
		x_adj = x + 1
		y_adj = y
	elif z==1:
		x_adj = x - 1
		y_adj = y
	elif z==1:
		x_adj = x
		y_adj = y + 1
	else:
		x_adj = x 
		y_adj = y - 1

	if x_adj >= L or x_adj < 0 or y_adj >= L or y_adj < 0:			# if the location exceeds the grid choose a diff random site 
		i = i - 1													#Do not count the step
		continue		
	if mat[y][x] != 1 and mat[y_adj][x_adj] != 1:					#checking wheather the site is empty
		mat[y][x] = 1												#If the site is empty  set it as 1
		mat[y_adj][x_adj] = 1
		col[0] = y
		row[0] = x
		col[1] = y_adj
		row[1] = x_adj
		plt.plot(col,row,color='b',marker = 'o',linestyle='-')

plt.savefig('9_dimmer.png', bbox_inches = 'tight')
plt.show()



