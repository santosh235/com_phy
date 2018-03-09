# -*- coding: PYTHON3 -*-
# @Author: Santosh
# @Last Modified by:   Santosh


""" COMPARISON OF DFT AND DCT"""


import matplotlib.pyplot as plt
import numpy as np
import math
from dcst import dct, idct



# READING DATA FROM DOW2.TXT AND STORING IT IN ARRAY
f1 = open('dow2.txt', 'r')
lines = f1.readlines()
y_dow2 = []
for line in lines:
    p = line.split()
    y_dow2.append(float(p[0]))
y_dow2 = np.array(y_dow2)
t_dow2 = np.linspace(0, 2*math.pi, len(y_dow2))

#DFT
#REAL FOURIER TRANSFORM OF THE DOW.TXT
fk_dow2 = np.fft.rfft(y_dow2)
freq_dow2 = np.fft.rfftfreq(t_dow2.shape[-1])


#SETTING THE LAST 98 % OF THE FOURIER COEFFIECIENTS TO ZERO
for i in range(len(freq_dow2)):
	if i >  (0.02 * len(freq_dow2)):
		fk_dow2[i] = 0

ft_inverse_2 = np.fft.irfft(fk_dow2)


#PLOTTING THE DATA FILE AS WELL AS THE FOURIER TRANSFORM WHERE LAST 90%  OF COEFFICIENTS IS SET TO ZERO
plt.xlabel('Time')
plt.ylabel(r'$f(t)$')
plt.title('DFT::Original data and last "98%" freq set to zero')
plt.plot(t_dow2,y_dow2,'b', label = 'original data')
plt.plot(t_dow2,ft_inverse_2,'r', label = 'Higher freq set to zero')
plt.legend(fontsize = 'x-small')
plt.savefig('dow2_dft.png',bbox_inches = 'tight')
plt.show()
plt.clf()

#DCT
fk_dct_dow2 = dct(y_dow2)

#SETTING THE LAST 98 % OF THE FOURIER COEFFIECIENTS TO ZERO
for i in range(len(freq_dow2)):
	if i >  (0.02 * len(freq_dow2)):
		fk_dct_dow2[i] = 0

ft_dct_inverse_2 = idct(fk_dct_dow2)


#PLOTTING THE DATA FILE AS WELL AS THE FOURIER TRANSFORM WHERE LAST 90%  OF COEFFICIENTS IS SET TO ZERO
plt.xlabel('Time')
plt.ylabel(r'$f(t)$')
plt.title('DCT::Original data and last "98%" freq set to zero')
plt.plot(t_dow2,y_dow2,'b', label = 'original data')
plt.plot(t_dow2,ft_dct_inverse_2,'r', label = 'Higher freq set to zero')
plt.legend(fontsize = 'x-small')
plt.savefig('dow2_dct.png',bbox_inches = 'tight')
plt.show()