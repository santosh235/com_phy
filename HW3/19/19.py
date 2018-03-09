 
import math
import matplotlib.pyplot as plt

h =30000
file = []
with open("altitude.txt","r") as f:
	lines = f.readlines()
	for line in lines:
		file.append([float(x) for x in line.split(" ")])
	
for j in range(1,512):
	for i in range(1,len(mat)):
		if i == len(mat):
			x_der = (mat[j][1] - mat[j][i])/h
		else:
			x_der = (mat[j][i+1] - mat[j][i])/h


for i in range(1,len(B)):
	for j in range(1,512):
		if j == 512:
			y_der = (mat[1][i] - mat[j][i])/h
		else:
			y_der = (mat[j+1][i] - mat[j][i])/h


#Intensity
I = (x_der +y_der)/math.sqrt(2* (x_der)^2 + (y_der)^2 +1)

plt.pcolor(x, y, mat, cmap='RdBu')
plt.show()