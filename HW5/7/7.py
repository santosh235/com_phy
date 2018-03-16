# -*- coding: utf-8 -*-
# @Author: santosh
# @Date:   2018-03-15 17:55:12
# @Last Modified by:   santosh
# @Last Modified time: 2018-03-15 19:06:24


""" Ising Model """

import numpy as np 
import random
from math import exp
import matplotlib.pyplot as plt

def Energy(J,config, L):

	padded_config = [[0 for x in range(L+2)] for y in range(L+2)]
	for i in range(L):
		for j in range(L):
			padded_config[i+1][j+1] = config[i][j]
	E = 0
	for i in range(1,L+1):
		for j in range(1,L+1):
			E = E + padded_config[i][j]*padded_config[i-1][j] + padded_config[i][j]*padded_config[i+1][j] + padded_config[i][j]*padded_config[i][j-1] + padded_config[i][j]*padded_config[i][j+1]

	E = float((-J * E) / 2)	# To remove double counting

	return E

def Magnetization(config, L):
	M = 0
	for i in range(L):
		for j in range(L):
			M = M + config[i][j]
	return M

def probability(E_new , E_old , k, T):
	roll = random.uniform(0,1)
	beta = 1.0 / (k * T)
	p = exp(-beta * (E_new - E_old))

	if roll < p:
		prob = 1.0
	else:
		prob = 0.0
	return prob


L = 20
J = 1
k = 1
T = 1
N = 100000
M = []
time = np.arange(0,N,1)
config = np.zeros((L,L))


for i in range(L):
	for j in range(L):
		x = random.randint(0,1)
		if x == 0 :
			x = -1

		config[i][j] = x


for i in range(N):
	E_old = Energy(J , config, L)

	rand_i = random.randint(0, L-1)
	rand_j = random.randint(0, L-1)

	config[rand_i][rand_j] = -1*config[rand_i][rand_j]

	E_new = Energy(J , config, L)

	if E_new >= E_old:
		prob = probability(E_new, E_old ,k , T)
		if prob == 0.0:
			config[rand_i][rand_j] = -1*config[rand_i][rand_j]

	M.append(Magnetization(config, L))



plt.plot(time,M)
plt.xlabel(r'Time')
plt.ylabel(r'Magnetization')
plt.title(r'Magnetization Vs Time')
plt.savefig('7_magnetization_vs_time.png' ,bbox_inches='tight')
plt.show()