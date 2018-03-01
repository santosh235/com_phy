#Least square fitting
import matplotlib.pyplot as plt
import numpy as np

f1=open('millikan.txt','r')
lines=f1.readlines()

x1=[]
y1=[]

for line in lines:
    p=line.split()
    x1.append(float(p[0]))
    y1.append(float(p[1]))

xv=np.array(x1)
yv=np.array(y1)

plt.title('Milikan Experiment data')
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(xv,yv)
plt.savefig('Milikan_1.png')
plt.clf()

l=len(x1)
E_x=0
E_y=0
E_xx=0
E_xy=0

for i in range(0,l):
    E_x=x1[i]+E_x
    E_y=y1[i]+E_y
    E_xx=x1[i]*x1[i]+E_xx
    E_xy=x1[i]*y1[i]+E_xy

E_x=E_x/l
E_y=E_y/l
E_xx=E_xx/l
E_xy=E_xy/l

m=(E_xy-(E_x*E_y))/(E_xx-(E_x*E_x))
c=((E_xx*E_y)-(E_x*E_xy))/(E_xx-(E_x*E_x))

print("The slope is :"+str(m))
print("The intercept is :%f" %c)

x = np.linspace(0.5e+15, 1.3e+15, 50)
y=m*x+c
plt.title('Milikan Experiment data and least square fit')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,label='Least square fit')
plt.scatter(xv,yv,label='data points')
plt.legend()
plt.savefig('Milikan_2.png')

h=m*(1.602e-19)
print("Value of planck's constant:"+str(h))
