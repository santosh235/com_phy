# SUNSPOTS
import matplotlib.pyplot as plt
import numpy as np
f1 = open('sunspots.txt', 'r')
lines = f1.readlines()
x1 = []
y1 = []
i = 0
for line in lines:
    p = line.split()
    x1.append(float(p[0]))
    y1.append(float(p[1]))
xv = np.array(x1)
yv = np.array(y1)

plt.plot(xv, yv)
plt.title("Original data for sunspots")
plt.savefig('13_sunspots_1.png')
plt.clf()
plt.plot(xv[0:1000], yv[0:1000])
plt.title("Original data for sunspots(First 1000 points)")
plt.savefig('13_sunspots_2.png')
plt.clf()

l = len(xv)
x2 = x1[:]
y2 = y1[:]
for i in range(5, l - 5):
    y2[i] = 0

for k in range(5, l - 5):
    for m in range(-5, 6):
        y2[k] = y1[k + m] + y2[k]
    y2[k] = y2[k] / 10

fig, ax = plt.subplots(nrows=2, ncols=1)
plt.suptitle("Comparison between original data and running average")

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'b', label="Original data")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r', label="Running average")
plt.legend()

plt.savefig('13_sunspots_3.png')
plt.clf()


fig, ax = plt.subplots(nrows=2, ncols=1)
plt.suptitle(
    "Comparison between original data and running average(first 1000 points)")

plt.subplot(2, 1, 1)
plt.plot(x1[0:1000], y1[0:1000], 'b', label="Original data")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x2[0:1000], y2[0:1000], 'r', label="Running average")
plt.legend()

plt.savefig('13_sunspots_4.png')
plt.clf()
