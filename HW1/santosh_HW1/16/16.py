#Chaos
import matplotlib.pyplot as plt

def map1(r,x):
    r=float(r)
    x=float(x)
    for i in range(0,2001):
        x=r*x*(1.0-x)
    return x

def map2(r,x):
    r=float(r)
    x=float(x)
    for i in range(0,2002):
        x=r*x*(1.0-x)
    return x

r=[None] * 402
x=[None] * 402
y=[None] * 402

r[0]=0.0
z=0.5

for i in range(0,401):
    x[i]=map1(r[i],z)
    y[i]=map2(r[i],z)
    r[i+1]=r[i]+0.01

plt.scatter(r,x,c='b', marker='x', label='1')
plt.scatter(r,y,c='r', marker='*', label='-1')
plt.legend(loc='upper left')

plt.xlabel('r')
plt.ylabel('x')
plt.title('Figtree plot')
plt.savefig('Figtree plot')
plt.show()
