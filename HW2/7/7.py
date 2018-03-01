"""Energy levels"""
from pylab import *
import math




Xi=4.58434


x_max=4.6
x=arange(0.01,x_max,0.01)
y=[]
w=[]
z=[]
for i in x:
	y.append(math.tan(i))


for k in x:
	cot = 1/math.tan(k)
	z.append(-cot)

for j in x:
	arg = pow(Xi/j, 2) - 1
	if arg > 0:
		arg = pow(arg, 0.5)
		w.append(arg)
	else:
		w.append(0)



xlim(0,x_max)
ylim(0,10)
plot(x,y,label='tan(eta)')
plot(x,z,label='-cot(eta)')
plot(x,w)
title('The intersection gives the solution to the  roots:')
legend()
savefig('7_eigenvalues.png')

def even(eta,Xi):
	arg = pow(Xi/eta, 2) - 1
	if arg >= 0:
		f=math.tan(eta)-pow(arg,0.5)
		return f
	else:
		return 0

def odd(eta,Xi):
	arg = pow(Xi/eta, 2) - 1
	if arg >= 0:
		f=(1/math.tan(eta))+pow(arg,0.5)
		return f
	else:
		return 0

def root(a,b):
	if 