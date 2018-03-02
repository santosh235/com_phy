""" Fourier filtering and smoothing"""

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
t_dow = np.linspace(0, 2*math.pi, len(y_dow))

fk_dow = np.fft.rfft(y_dow)
freq_dow = np.fft.rfftfreq(t_dow.shape[-1])
fk_dow_abs = []

for i in range(len(freq_dow)):
	fk_dow_abs.append(math.hypot(fk_dow.real[i],fk_dow.imag[i]))

plt.suptitle("DOW file and its fourier transform")
plt.subplot(211)
plt.plot(t_dow,y_dow)
plt.xlabel('Time')
plt.ylabel(r'$f(t)$')

plt.subplot(212)
plt.xlabel(r'$k$')
plt.ylabel(r'$F(k)$')
plt.plot(freq_dow,fk_dow_abs)
# plt.savefig('dow.png',bbox_inches = 'tight')
# plt.clf()
plt.show()


fk_dow_abs_zero = []

for i in range(len(freq_dow)):
	if i <  (0.1 * len(freq_dow)):
		fk_dow_abs_zero.append(fk_dow[i])
		
	else:
		fk_dow_abs_zero.append(float(0))

ft_inverse_10 = np.fft.irfft(fk_dow_abs_zero)
plt.xlabel('Time')
plt.ylabel(r'$f(t)$')

# plt.plot(t_dow,y_dow,'b')
plt.plot(t_dow,ft_inverse_10,'r')
plt.show()


for i in range(len(freq_dow)):
	if i >  (0.02 * len(freq_dow)):
		fk_dow_abs_zero[i] = 0

ft_inverse_2 = np.fft.irfft(fk_dow_abs_zero)

plt.xlabel('Time')
plt.ylabel(r'$f(t)$')

# plt.plot(t_dow,y_dow,'b')
plt.plot(t_dow,ft_inverse_2,'r')
plt.show()



N = np.linspace(0,1,1000)

ft_sq = signal.square(2*math.pi*N)

fk_sq = np.fft.rfft(ft_sq)
# fk_sq_abs = []

for i in range(10,len(fk_sq)):
	fk_sq[i] = 0

ft_inverse_sq = np.fft.irfft(fk_sq)
plt.plot(N,ft_sq)
plt.plot(N,ft_inverse_sq)
plt.ylim(-2,2)
plt.show()
