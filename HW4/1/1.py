""" fourier transform of simple function"""

import matplotlib.pyplot as plt 
from numpy import fft, linspace,pi,sin
from scipy import signal
import math


t = linspace(0,2*pi,1000) 		# ARRAY OF 1000 EVENLY SPACED POINTS FROM 0 TO 2PI
freq = fft.fftfreq(t.shape[-1]) 		#FREQUENCY DOMAIN
N = 1000



#SQUARE WAVE AND ITS TRANSFORM
ft_sq = signal.square(10*pi*t,0.5) 		#SQUARE WAVE GENERATION
fk_sq = fft.fft(ft_sq) 		#FOURIER COEFFIECIENTS OF SQUARE WAVE

#ABSOLUTE VALUE
fk_sq_abs = []
for i in range(1000):
	fk_sq_abs.append(math.hypot(fk_sq.real[i],fk_sq.imag[i]))

#DATA PLOTTING
plt.suptitle("Square wave and its fourier transform")
plt.subplot(211,)
plt.plot(t,ft_sq)
plt.xlabel('Time')
plt.ylabel(r'$f(t)$')

plt.subplot(212)
plt.xlabel(r'$k$')
plt.ylabel(r'$F(k)$')
plt.plot(freq,fk_sq_abs)
plt.savefig('square.png' , bbox_inches='tight')
plt.clf()



#SAWTOOTH WAVE AND ITS TRANSFORM
ft_saw = signal.sawtooth(2*pi*t)			#SAWTOOTH WAVE GENERATION
fk_saw = fft.fft(ft_saw)			#FOURIER COEFFICIENTS OF SAWTOOTH WAVE

#ABSOLUTE VALUE
fk_saw_abs = []
for i in range(1000):
	fk_saw_abs.append(math.hypot(fk_saw.real[i],fk_saw.imag[i]))

#DATA PLOTTING
plt.suptitle("Sawtooth wave and its fourier transform")
plt.subplot(211)
plt.plot(t,ft_saw)
plt.xlabel('Time')
plt.ylabel(r'$f(t)$')

plt.subplot(212)
plt.xlabel(r'$k$')
plt.ylabel(r'$F(k)$')
plt.plot(freq,fk_saw_abs)
plt.savefig('sawtooth.png' , bbox_inches='tight')
plt.clf()

# MODULATED SINE WAVE AND ITS TRANSFORM
ft_sin = []
for n in range(1000):
	ft_sin.append(sin(pi*n/N) * sin(20 * pi * n / N)) #MODULATED SINE WAVE


fk_sin = fft.fft(ft_sin) 		#FOURIER COEFFICIENTS OF MODULATED SINE WAVE

fk_sin_abs = []
for i in range(1000):
	fk_sin_abs.append(math.hypot(fk_sin.real[i],fk_sin.imag[i]))

#DATA PLOTTING
plt.suptitle("Modulated sine wave and its fourier transform")
plt.subplot(211)
plt.xlim(0,2*math.pi)
plt.plot(t,ft_sin)
plt.xlabel('Time')
plt.ylabel(r'$f(t)$')

plt.subplot(212)
plt.xlabel(r'$k$')
plt.ylabel(r'$F(k)$')
plt.xlim(-0.3,0.3)
plt.plot(freq,fk_sin_abs)
plt.savefig('modulated_sine_wave.png' , bbox_inches='tight')
