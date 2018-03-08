# -*- coding: PYTHON3 -*-
# @Author: Santosh
# @Last Modified by:   Santosh


""" Fourier transform of musical instruments"""

import matplotlib.pyplot as plt
import numpy as np
import math

# READING DATA FROM PIANO.TXT AND STORING IT IN ARRAY
f1 = open('piano.txt', 'r')
lines = f1.readlines()
y_piano = []
for line in lines:
    p = line.split()
    y_piano.append(float(p[0]))
y_piano = np.array(y_piano)
t_piano = np.linspace(0, 2*math.pi, len(y_piano))


#REAL FOURIER TRANSFORM
fk_piano = np.fft.rfft(y_piano)
freq_piano = np.fft.rfftfreq(t_piano.shape[-1])
fk_piano_abs = []

for i in range(len(freq_piano)):
	fk_piano_abs.append(math.hypot(fk_piano.real[i],fk_piano.imag[i]))

#PLOTTING THE PIANO.TXT FILE AND ITS FOURIER TRANSFORM
plt.suptitle("Piano file and its fourier transform")
plt.subplot(211)
plt.plot(t_piano,y_piano)
plt.xlabel('Time')
plt.ylabel(r'$f(t)$')

plt.subplot(212)
plt.xlabel(r'$k$')
plt.ylabel(r'$F(k)$')
plt.plot(freq_piano[0:10000],fk_piano_abs[0:10000])
plt.savefig('piano.png',bbox_inches = 'tight')
plt.show()
plt.clf()




# READING DATA FROM TRUMPET.TXT AND STORING IT IN ARRAY
f2 = open('trumpet.txt', 'r')
lines = f2.readlines()
y_trumpet = []
for line in lines:
    p = line.split()
    y_trumpet.append(float(p[0]))
y_trumpet = np.array(y_trumpet)
t_trumpet = np.linspace(0, 2*math.pi, len(y_trumpet))


#REAL FOURIER TRANSFORM
fk_trumpet = np.fft.rfft(y_trumpet)
freq_trumpet = np.fft.rfftfreq(t_trumpet.shape[-1])
fk_trumpet_abs = []

for i in range(len(freq_trumpet)):
	fk_trumpet_abs.append(math.hypot(fk_trumpet.real[i],fk_trumpet.imag[i]))


#PLOTTING THE TRUMPET.TXT FILE AND ITS FOURIER TRANSFORM
plt.suptitle("Trumpet file and its fourier transform")
plt.subplot(211)
plt.plot(t_trumpet,y_trumpet)
plt.xlabel('Time')
plt.ylabel(r'$f(t)$')

plt.subplot(212)
plt.xlabel(r'$k$')
plt.ylabel(r'$F(k)$')
plt.plot(freq_trumpet[0:10000],fk_trumpet_abs[0:10000])
plt.savefig('trumpet.png',bbox_inches = 'tight')
plt.show()
plt.clf()