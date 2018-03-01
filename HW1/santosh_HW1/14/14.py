# Curve plotting
# round(math.cos(math.radians(45)),2)
import matplotlib.pyplot as plt
import numpy as np
import math


def cartesian_x(r, phi):
    cos_theta = round(math.cos(phi), 3)
    x = r * cos_theta
    return x


def cartesian_y(r, phi):
    sin_theta = round(math.sin(phi), 3)
    y = r * sin_theta
    return y


x1 = [None] * 100001
y1 = [None] * 100001
pi = math.pi

for i in range(0, 100001):
    theta = (2 * pi / 100000) * i
    cos_theta = round(math.cos(theta), 3)
    cos_2theta = round(math.cos(2 * theta), 3)
    sin_theta = round(math.sin(theta), 3)
    sin_2theta = round(math.sin(2 * theta), 3)
    x1[i] = (2 * cos_theta) + (cos_2theta)
    y1[i] = (2 * sin_theta) - (sin_2theta)

plt.title('Deltoid_curve')
plt.plot(x1, y1)
plt.savefig('Deltoid_curve.png')

# Galilean Curve
for i in range(0, 100001):
    theta = (pi / 10000) * i
    r = theta * theta
    x1[i] = cartesian_x(r, theta)
    y1[i] = cartesian_y(r, theta)
plt.title('Galilean Spiral')
plt.plot(x1, y1)
plt.savefig('Galilean_spiral.png')


# FEY'S FUNCTION
for i in range(0, 100001):
    theta = (24 * pi / 100000) * i
    cos_theta = round(math.cos(theta), 3)
    e_cos = math.exp(cos_theta)
    cos_4theta = round(math.cos(4 * theta), 3)
    sin_5 = (round(math.sin(theta / 12), 3))**5
    r = e_cos - 2 * cos_4theta + sin_5
    x1[i] = cartesian_x(r, theta)
    y1[i] = cartesian_y(r, theta)
plt.title("Fey's function")
plt.plot(x1, y1)
plt.savefig('Fey_function.png')
