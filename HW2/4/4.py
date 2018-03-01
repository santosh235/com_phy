"""Fixed point Iteration Method."""
import math
import matplotlib.pyplot as plt


def fix_point(c, x):
    x1 = 1 - math.exp(-c * x)
    return x1


def result(c, x_old):
    x_new = fix_point(c, x_old)
    while(True):
        if abs(x_new - x_old) < 10e-8:
            break
        else:
            x_old = x_new
            x_new = fix_point(c, x_old)
    return x_new


x_init = 1.0
print(" Root:: %.6f " %(result(2.0, x_init)))


c = [None] * 301
x = [None] * 301

for i in range(0, 301):
    c[i] = i * 0.01
    x[i] = result(c[i], x_init)

plt.xlabel('c')
plt.ylabel('x')
plt.title('percolation transition')
plt.plot(c, x)
plt.savefig('percolation transition.png')

