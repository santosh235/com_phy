"""FAST FOURIER TRANSFORM USING PERSONAL WRIITEN FFT CODE"""

import numpy as np
import matplotlib.pyplot as plt
import math


# ALGORITHM FOR FFT 

def FFT_coded(x):
    
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if np.log2(N) % 1 > 0:
        raise ValueError("size of x must be a power of 2")

    N_min = min(N, 32)   #N_min SHOULD BE POWER OF TWO
    
    # Perform an O[N^2] DFT on all length-N_min sub-problems at once
    n = np.arange(N_min)
    k = n[:, None]
    M = np.exp(-2j * np.pi * n * k / N_min)
    X = np.dot(M, x.reshape((N_min, -1)))

    
    while X.shape[0] < N:
        X_even = X[:, :X.shape[1] / 2]
        X_odd = X[:, X.shape[1] / 2:]
        factor = np.exp(-1j * np.pi * np.arange(X.shape[0])
                        / X.shape[0])[:, None]
        X = np.vstack([X_even + factor * X_odd,
                       X_even - factor * X_odd])

    return X.ravel()

# READING DATA FROM PITCH.TXT AND STORING IT IN ARRAY
f1 = open('pitch.txt', 'r')
lines = f1.readlines()
y_pitch = []
for line in lines:
    p = line.split()
    y_pitch.append(float(p[0]))
y_pitch = np.array(y_pitch)
t_pitch = np.linspace(0, 2*math.pi, len(y_pitch))



#USING THE CONVENTIONAL NUMPY PACKAGE TO DO FFT
fk = np.fft.rfft(y_pitch)
freq = np.fft.rfftfreq(t_pitch.shape[-1])
fk_abs = []

for i in range(len(freq)):
    fk_abs.append(math.hypot(fk.real[i],fk.imag[i]))


# USING THE ABOVE DEFINITION OF FFT
fk_code = FFT_coded(y_pitch)
fk_code_abs =[]
for i in range(len(freq)):
    fk_code_abs.append(math.hypot(fk_code.real[i],fk_code.imag[i]))


#PLOTTING THE DATA
#ORIGINAL DATA FILE
plt.suptitle("PITCH file and its fourier transform")
plt.subplot(311)
plt.plot(t_pitch,y_pitch, label = 'original data')
plt.xlabel('Time')
plt.ylabel(r'$f(t)$')

# FOURIER TRANSFORM USING THE ABOVE ALGORITH
plt.subplot(312)
plt.xlabel(r'$k$')
plt.ylabel(r'$F(k)$')
plt.plot(freq,fk_code_abs, label ='coded fft')
plt.legend()

# FOURIER TRANSFORM USING THE NUMPY FFT
plt.subplot(313)
plt.xlabel(r'$k$')
plt.ylabel(r'$F(k)$')
plt.plot(freq,fk_abs, label ='numpy fft')
plt.legend()

plt.savefig('pitch.png',bbox_inches = 'tight') #SAVING THE FIGURE TO FILE
plt.show()
