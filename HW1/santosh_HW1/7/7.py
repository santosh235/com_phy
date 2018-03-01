#Q7: Catalan Numbers
n=0
C_n=1
print("The catalan numbers are::")
while C_n < 1000000000:
	C_n=int(C_n)
	print(C_n)
	C_n_1=((4*n+2)*C_n)/(n+2)
	C_n=C_n_1
	n=n+1
