#Binding energy

def binding(Z,A):
	a1=15.67
	a2=17.23
	a3=0.75
	a4=93.2
	if A%2!=0:
		a5=0
	elif A%2==0 and Z%2==0:
		a5=12
	else :
		a5=-12

	b1=a1*A

	b2=a2*(A**(2/3))
	b3=a3*(Z**2)/(A**(1/3))
	b4=a4*((A-2*Z)**2)/A
	b5=a5/(A**(1/2))

	B=b1-b2-b3-b4+b5
	return B

def bind_nuc(Z,A):
	B=binding(Z,A)/A
	return B

print("\nANSWER TO PART a")
Z=input("Enter Z ::")
A=input("Enter A::")
Z=float(Z)
A=float(A)

B_total=binding(Z,A)
print("The Binding energy is :"+str(B_total)+" MeV")

print("\nANSWER to PART b:")

B=bind_nuc(Z,A)

print("Binding energy per nucleons::"+str(B)+" Mev")

print("\nANSWER TO PART C")

Z=input("This time just enter the value of Z::")
Z=int(Z)
max1=0
for A in range(Z,(3*Z+1)):
	if bind_nuc(Z,A) > max1:
		A_stable=A
		max1=bind_nuc(Z,A)
print("Atomic mass for stable nucleus is :"+str(A_stable)+" and the binding energy  is :"+str(max1)+" MeV")




max1=0
a=0
A_stable=0
B_array=[None] * 101
B_array[0]=0
for Z in range(1,101):
	for A in range(Z,(3*Z+1)):
		if bind_nuc(Z,A) > max1:
			A_stable=A
			max1=bind_nuc(Z,A)
	B_array[Z]=max1
	max1=0
	print("Z=%d => A=%d" %(Z,A_stable))
B=max(B_array)
for i in range(0,len(B_array)):
	if B_array[i]==B:
		Z=i
		break
print("The atomic number for maximum binding energy per nucleon is :%d" %Z)
