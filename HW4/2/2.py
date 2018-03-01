"""Detecting periodicityof sunspots"""

import matplotlib.pyplot as plt
import numpy as np
import math

# READING DATA FROM FILE AND STORING IT IN ARRAY
f1 = open('sunspots.txt', 'r')
lines = f1.readlines()
x1 = []
y1 = []
i = 0
for line in lines:
    p = line.split()
    x1.append(float(p[0]))
    y1.append(float(p[1]))
xv = np.array(x1)
yv = np.array(y1)

#DATA PLOTTING
plt.plot(xv,yv)
plt.xlabel('Time (months)')
plt.ylabel('sunspots number')
plt.title("Original data for sunspots")
plt.savefig('2_sunspots_1.png' , bbox_inches='tight')
plt.clf()

print("The estimated periodicity is : 124 months" )

#POWER SPECTRUM CALCULATION
fk = np.fft.fft(yv)
freq = np.fft.fftfreq(xv.shape[-1])
fk_abs = []

for i in range(len(xv)):
	fk_abs.append(abs(fk[i] * fk[i].conjugate()))

#PLOTTING POWER SPECTRUM
plt.plot(freq,fk_abs)
plt.xlabel(r'$k$')
plt.ylabel(r'$c_k^2$')
plt.xlim(-0.2,0.2)
plt.ylim(0,0.5e10)
plt.title('Power Spectrum')
plt.savefig('2_sunspots_2_power_spectrum.png' , bbox_inches='tight')
plt.clf()


#CREATING SINE WAVE OF FREQ SAME AS THE ONE WE GET FROM POWER SPECTRUM
sin_wave = np.sin(2*math.pi*0.008*xv)

#SUBPLOT- ORIGINAL DATA AND THE SINE WAVE
plt.subplot(211)
plt.plot(xv, yv,'-',c = 'b')
plt.xlabel('Time (months)')
plt.ylabel('sunspots number')
plt.title("Original data for sunspots")


plt.subplot(212)
plt.plot(xv,sin_wave)
plt.xlabel('Time')
plt.ylabel('sine wave')
plt.title('Sine wave of freq = 0.008')
plt.savefig('2_sunspots_3.png' , bbox_inches='tight')
plt.clf()
