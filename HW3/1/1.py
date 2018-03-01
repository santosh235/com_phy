"Velocity and Displacement"

import matplotlib.pyplot as plt
import numpy as np


f1 = open('velocities.txt', 'r')
lines = f1.readlines()
t = []
vel = []
dis = []
for line in lines:
    p = line.split()
    t.append(float(p[0]))
    vel.append(float(p[1]))

del_x = t[1] - t[0]
l = len(t)
print(l)

f2=open('displacement.txt','w')

for i in range(0,l):
	a = 0.0
	for j in range(0,i):
		a = a + vel[j]

	a = (vel[0] + vel[i] + 2*a)/2
	dis.append(float(a))
	f2.write("%d     %f\n" %(t[i],dis[i]))

plt.subplot(211)
plt.plot(t,vel,label = 'Velocity-time graph')
plt.legend(fontsize=10)
plt.xlabel('Time')
plt.ylabel('Velocity')

plt.subplot(212)
plt.plot(t,dis, label = 'Displacement-time graph',c='r')
plt.suptitle("Velocity-time and dis-time graph")
plt.legend(fontsize=10)
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.savefig('1_Vel_dis_graph.png',bbox_inches='tight')
