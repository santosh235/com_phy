#PRIME NUMBERS
import math
print("PRIME NUMBERS::")
list=[2]
flag=0
for n in range(3,10001):
	for i in list:
		if i > math.sqrt(n):
			break
		if n%i==0:
			flag=1
	if flag==1:
		flag=0
	else:
		list.append(n)

print(list)
	

