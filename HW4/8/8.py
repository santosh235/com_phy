# -*- coding: PYTHON3 -*-
# @Author: Santosh
# @Last Modified by:   Santosh


""" Image Deconvolution"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import math



#FUNCTION THAT CALCULATES POINT SPREAD FUNCTION
def gauss(x,y):
	d = np.sqrt(x*x+y*y)
	sigma= 25.0
	g = np.exp(-( (d)**2 / ( 2.0 * sigma**2 ) ) )
	return g


#GRID SIZE
x=1024 
y=1024

#READING DATA FROM BLUR.TXT
raw_text = open("blur.txt").read()
blocks = raw_text.split("\n")
split_blicks = [[float(v) for v in block.split()]  for block in blocks]


a=[]								#create an empty list first
for i in range(x):
    a.append([0]*y)    				#And again append empty lists to original list
    for j in range(y):
         a[i][j]= split_blicks[i][j]


#SHOWING THE BLUR IMAGE
plt.imshow(a, cmap='gray', interpolation='nearest')
plt.title("Blurred image")
plt.savefig("blurred_image.png", bbox_inches = 'tight')
plt.show()


# CREATING A ZERO 2D ARRAY
g_mat = []
for i in range(x):
	g_mat.append([0]*y)
	for j in range(y):
		g_mat[i][j] = 0

#CALCULATING THE POINT SPREAD FUNCTION

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


#SHOWING THE POINT SPREAD FUNCTION
plt.imshow(g_mat, cmap='gray', interpolation='nearest')
plt.title("point spread function")
plt.savefig("point_spread_function.png", bbox_inches = 'tight')
plt.show()



#FOURIER TRANSFORM OF BLUR IMAGE AS WELL AS POINT SPREAD FUNCTION
fk_image = np.fft.rfft2(a)
fk_psf = np.fft.rfft2(g_mat)

fk_image_abs = []
for i in range(1024):
	fk_image_abs.append([0]*513)
	for j in range(513):
		fk_image_abs[i][j] =(math.hypot(fk_image.real[i][j],fk_image.imag[i][j]))



fk_psf_abs = []
for i in range(1024):
	fk_psf_abs.append([0]*513)
	for j in range(513):
		fk_psf_abs[i][j] =(math.hypot(fk_psf.real[i][j],fk_psf.imag[i][j]))



fk_unblur = []
for i in range(1024):
	fk_unblur.append([0]*513)
	for j in range(513):
		if fk_psf_abs[i][j] != 0:
			fk_unblur[i][j] = fk_image_abs[i][j] / fk_psf_abs[i][j]
		else:
			fk_unblur[i][j] = fk_image_abs[i][j]

#INVERSE FOURIER TRANSFORM
ft_unblur = np.fft.irfft2(fk_unblur)
# plt.imshow(ft_unblur, cmap='gray', interpolation='nearest')
# plt.show()