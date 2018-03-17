# -*- coding: utf-8 -*-
# @Author: santosh
# @Date:   2018-03-15 23:56:37
# @Last Modified by:   santosh

""" RADIO_ACTIVE DECAY """

import numpy as np 
import matplotlib.pyplot as plt


#Functional defination of pdf of decay
def pdf(t,tau):

	p = 1 - 2 ** (-(t / tau))
	return p

Time = 20000	# Running the process for 20000 seconds
xmin = 0
xmax = 1
pmin = 0
pmax = 1

#Initial number of all the four isotopes
N_Bi_213_tot = 10000
N_Pb_209_tot = 0
N_Ti_209_tot = 0
N_Bi_209_tot = 0


# Half life in terms of seconds
tau_Bi_213 = 46 * 60
tau_Ti_209 = 2.2 * 60
tau_Pb_209 = 3.3 * 60

#Array of points to keep track of number of individual isotopes  as function of time
N_Bi_213 = np.zeros(Time)
N_Pb_209 = np.zeros(Time)
N_Ti_209 = np.zeros(Time)
N_Bi_209 = np.zeros(Time)

# Number of atom of each type at t=0
N_Bi_213[0] = 10000
N_Pb_209[0] = 0
N_Ti_209[0] = 0
N_Bi_209[0] = 0


#array of time
t = np.arange(0,Time,1)

# Running the lopp for the prescribed time
for i in range(Time):

	#Decay of Pb-209
	N = 0
	for n in range(N_Pb_209_tot):
		x = np.random.uniform(xmin,xmax)
		y = np.random.uniform(pmin,pmax)

		if y < pdf(x,tau_Pb_209):
			N = N + 1
	#Updating the corresponding number
	N_Bi_209_tot = N_Bi_209_tot + N
	N_Bi_209[i] = N_Bi_209[i] + N
	N_Pb_209_tot = N_Pb_209_tot - N
	N_Pb_209[i] = N_Pb_209[i] - N 

	#Decay of Ti-209
	N = 0
	for n in range(N_Ti_209_tot):
		x =  np.random.uniform(xmin,xmax)
		y = np.random.uniform(pmin,pmax)
		if y < pdf(x,tau_Ti_209):
			N = N + 1
	
	#Updating the corresponding number
	N_Pb_209_tot = N_Pb_209_tot + N 
	N_Pb_209[i]  = N_Pb_209[i] + N 
	N_Ti_209_tot =   N_Ti_209_tot - N 
	N_Ti_209[i] = N_Ti_209[i] - N

	#Decay of Bi-213
	N = 0
	M = 0
	for n in range(N_Bi_213_tot):

		x = np.random.uniform(xmin,xmax)
		y = np.random.uniform(pmin,pmax)

		if y < pdf(x,tau_Ti_209):
			z = np.random.uniform(xmin,xmax)
			if z < 0.9791:
				N = N + 1
			else:
				M = M + 1
	#Updating the corresponding number
	N_Pb_209_tot = N_Pb_209_tot + N
	N_Ti_209_tot = N_Ti_209_tot + M
	N_Bi_213_tot = N_Bi_213_tot - (N + M)
	N_Pb_209[i] = N_Pb_209[i] + N
	N_Ti_209[i] = N_Ti_209[i] + M
	N_Bi_213[i] = N_Bi_213[i] - (N + M)

	# updating the succeding array of each species for the next run
	if i != 19999:
		N_Bi_213[i+1] = N_Bi_213_tot
		N_Ti_209[i+1] = N_Ti_209_tot
		N_Pb_209[i+1] = N_Pb_209_tot
		N_Bi_209[i+1] = N_Bi_209_tot


#Data plotting
plt.plot(t,N_Bi_213, label = 'Bi_213')
plt.plot(t,N_Ti_209, label = 'Ti_209')
plt.plot(t,N_Pb_209, label = 'Pb_209')
plt.plot(t,N_Bi_209, label = 'Bi_209')
plt.title('Radioactive disintegration of Bi-213')
plt.xlabel(r'$Time$')
plt.ylabel(r'$Number$')
plt.legend()
plt.savefig('radioactivity.png' , bbox_inches = 'tight')
plt.show()
