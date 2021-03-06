# -*- coding: PYTHON3 -*-
# @Author: Santosh
# @Last Modified by:   Santosh


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
freq_dow = np.fft.rfftfreq(t_dow.shape[-1])
fk_dow_abs = []

for i in range(len(freq_dow)):
	fk_dow_abs.append(math.hypot(fk_dow.real[i],fk_dow.imag[i]))


#PLOTTING THE DATA FILE AS WELL AS THE FOURIER TRANSFORM
plt.suptitle("DOW file and its fourier transform")
plt.subplot(211)
plt.plot(t_dow,y_dow, label= 'original data')
plt.xlabel('Time')
plt.ylabel(r'$f(t)$')

plt.subplot(212)
plt.xlabel(r'$k$')
plt.ylabel(r'$F(k)$')
plt.ylim(0,0.2e6)
plt.plot(freq_dow,fk_dow_abs, label = 'Fourier transform')
plt.legend()
plt.savefig('dow_rfft.png',bbox_inches = 'tight')
plt.show()
plt.clf()



#SETTING THE LAST 90 % OF THE FOURIER COEFFIECIENTS TO ZERO
fk_dow_abs_zero = []
for i in range(len(freq_dow)):
	if i <  (0.1 * len(freq_dow)):
		fk_dow_abs_zero.append(fk_dow[i])
		
	else:
		fk_dow_abs_zero.append(float(0))


ft_inverse_10 = np.fft.irfft(fk_dow_abs_zero)

#PLOTTING THE DATA FILE AS WELL AS THE FOURIER TRANSFORM WHERE LAST 90%  OF COEFFICIENTS IS SET TO ZERO
plt.xlabel('Time')
plt.ylabel(r'$f(t)$')
plt.title('Original data and last "90%" freq set to zero')
plt.plot(t_dow,y_dow,'b', label = 'original data')
plt.plot(t_dow,ft_inverse_10,'r', label = 'Higher freq set to zero')
plt.legend()
plt.savefig('dow_rfft_10.png',bbox_inches = 'tight')
plt.show()
plt.clf()

#SETTING THE LAST 98 % OF THE FOURIER COEFFIECIENTS TO ZERO
for i in range(len(freq_dow)):
	if i >  (0.02 * len(freq_dow)):
		fk_dow_abs_zero[i] = 0

ft_inverse_2 = np.fft.irfft(fk_dow_abs_zero)


#PLOTTING THE DATA FILE AS WELL AS THE FOURIER TRANSFORM WHERE LAST 90%  OF COEFFICIENTS IS SET TO ZERO
plt.xlabel('Time')
plt.ylabel(r'$f(t)$')
plt.title('Original data and last "98%" freq set to zero')
plt.plot(t_dow,y_dow,'b', label = 'original data')
plt.plot(t_dow,ft_inverse_2,'r', label = 'Higher freq set to zero')
plt.legend()
plt.savefig('dow_rfft_2.png',bbox_inches = 'tight')
plt.show()
plt.clf()


#SQUARE WAVE

N = np.linspace(0,1,1000)
ft_sq = signal.square(2*math.pi*N)			#CREATING A SQUARE WAVE OF FREQ 1Hz
fk_sq = np.fft.rfft(ft_sq)					#REAL FOURIER TRANSFORM OF THE SQUARE WAVE


#SETTING ALL EXCEPT THE FIRST 10 COEFFICIENTS OF FOURIER TRANSFORM TO ZERO
for i in range(10,len(fk_sq)):
	fk_sq[i] = 0



#PLOTTING THE SQUARE WAVE AND ALSO THE INVERSE TRANSFORM
ft_inverse_sq = np.fft.irfft(fk_sq)
plt.plot(N,ft_sq, label = 'square wave')
plt.plot(N,ft_inverse_sq, label = 'All but the 1st ten cf set to zero')
plt.ylim(-2,2)
plt.legend()
plt.savefig('square_rfft.png',bbox_inches = 'tight')
plt.show()
