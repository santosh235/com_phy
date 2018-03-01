#MADELUNG CONSTANT
import math
def M_ijk(i,j,k):
	d=math.sqrt((i*i)+(j*j)+(k*k))
	flag=i+j+k
	if (flag%2)==1:
		d= -d
	m=1/d
	return m
M=0
for i in range(-80,80):
	for j in range(-80,80):
		for k in range(-80,80):
			if (i==0 and j==0 and k==0):
				continue

			M=M+M_ijk(i,j,k)
print(M)
