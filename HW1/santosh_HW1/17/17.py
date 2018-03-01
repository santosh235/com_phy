#MANDELBROT SET
import numpy as np
from PIL import Image

def show(data):
    img = Image.frombytes('1', data.shape[::-1], np.packbits(data, 1))
    img.show()
    img.save('mandelbrot.png')
n = 100
max = 100

M = np.zeros([n, n], np.uint8)
xvalues = np.linspace(-2, 2, n)
yvalues = np.linspace(-2, 2, n)

for u, x in enumerate(xvalues):
    for v, y in enumerate(yvalues):
        z = 0
        c = complex(x, y)
        for i in range(max):
            z = z*z + c
            if abs(z) > 2.0:
                M[v, u] = 1
                break

show(M)
