# -*- coding: utf-8 -*-
# @Author: Santosh
# @Date:   2018-03-02 22:20:24
# @Last Modified by:   Santosh
# @Last Modified time: 2018-03-03 00:53:02


""" Image Deconvolution"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def gauss(x,y):
	d = np.sqrt(x*x+y*y)
	sigma= 25.0
	g = np.exp(-( (d)**2 / ( 2.0 * sigma**2 ) ) )
	return g

x=1024
y=1024


# raw_text = open("blur.txt").read()
# blocks = raw_text.split("\n")
# split_blicks = [[float(v) for v in block.split()]  for block in blocks]


# a=[]								#create an empty list first
# for i in range(x):
#     a.append([0]*y)    				#And again append empty lists to original list
#     for j in range(y):
#          a[i][j]= split_blicks[i][j]

# plt.imshow(a, cmap='gray', interpolation='nearest')
# plt.show()

g_mat = []

for i in range(x):
	g_mat.append([0]*y)
	for j in range(y):
		g_mat[i][j] = 0



for i in range(x):
	for j in range(y):
		if i<512 and j< 512:
			g_mat[i][j] = gauss(i,j)
		elif i >= 512 and j <= 512:
			g_mat[i][j] = gauss(i-1023,j)
		elif i <= 512 and j >= 512 :
			g_mat[i][j] = gauss(i,j-1023)
		elif i > 512 and j > 512:
			g_mat[i][j] = gauss(i-1023,j-1023)

plt.imshow(g_mat, cmap='gray', interpolation='nearest')
plt.show()
