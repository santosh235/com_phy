""" Fourier filtering and smoothing"""

import matplotlib.pyplot as plt
import numpy as np
import math

# READING DATA FROM PIANO.TXT AND STORING IT IN ARRAY
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

# plt.suptitle("DOW file and its fourier transform")
# plt.subplot(211)
# plt.plot(t_dow,y_dow)
# plt.xlabel('Time')
# plt.ylabel(r'$f(t)$')

# plt.subplot(212)
# plt.xlabel(r'$k$')
# plt.ylabel(r'$F(k)$')
# plt.plot(freq_dow[0:10000],fk_dow_abs[0:10000])
# # plt.savefig('piano.png',bbox_inches = 'tight')
# plt.clf()
# plt.show()


fk_dow_abs_zero = []
j  = 0
for i in range(len(freq_dow)):
	if i <  (0.1 * len(freq_dow)):
		fk_dow_abs_zero.append(math.hypot(fk_dow.real[i],fk_dow.imag[i]))
		j = j+1
	else:
		fk_dow_abs_zero.append(float(0))


ft_inverse = np.fft.rfft(fk_dow_abs_zero)
print(len(ft_inverse))
time_inverse = np.fft.rfftfreq(freq_dow.shape[-1])

plt.xlabel('Time')
plt.ylabel(r'$f(t)$')

plt.plot(t_dow,y_dow,'b')
# plt.plot(time_inverse,ft_inverse,'r')
plt.show()