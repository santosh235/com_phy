# -*- coding: utf-8 -*-
# @Author: Santosh
# @Date:   2018-03-02 18:43:52
# @Last Modified by:   Santosh
# @Last Modified time: 2018-03-02 19:59:29



""" FOURIER FILTERING AND  SMOOTHING"""
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import signal


# READING DATA FROM DOW.TXT AND STORING IT IN ARRAY
f1 = open('dow.txt', 'r')
lines = f1.readlines()
y_dow = []
for line in lines:
    p = line.split()
    y_dow.append(float(p[0]))
y_dow = np.array(y_dow)
t_dow = np.linspace(0, 2*math.pi, len(y_dow)) 			#CREATING AN ARRAY OF POINTS (TIME)


#REAL FOURIER TRANSFORM OF THE DOW.TXT
fk_dow = np.fft.rfft(y_dow)
freq_dow = np.fft.fftfreq(t_dow.shape[-1])
fk_dow_abs = []

# for i in range(len(freq_dow)):
# 	fk_dow_abs.append(math.hypot(fk_dow.real[i],fk_dow.imag[i]))
print(len(t_dow))
print("\n\n")
print(len(freq_dow))

# #PLOTTING THE DATA FILE AS WELL AS THE FOURIER TRANSFORM
# plt.suptitle("DOW file and its fourier transform")
# plt.subplot(211)
# plt.plot(t_dow,y_dow, label= 'original data')
# plt.xlabel('Time')
# plt.ylabel(r'$f(t)$')

# plt.subplot(212)
# plt.xlabel(r'$k$')
# plt.ylabel(r'$F(k)$')
# plt.ylim(0,0.2e6)
# plt.plot(freq_dow,fk_dow_abs, label = 'Fourier transform')
# plt.legend()
# # plt.savefig('dow_rfft.png',bbox_inches = 'tight')
# plt.show()
# # plt.clf()