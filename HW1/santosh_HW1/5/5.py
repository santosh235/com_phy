#Quantum potential step
import math
E=10.0
V=9.0
h_bar=6.626e-34
m=9.11e-31
k1=(math.sqrt(2*m*E))/h_bar
k2=(math.sqrt(2*m*(E-V)))/h_bar

r=(k1-k2)/(k1+k2)
R=r*r
T=1-R
print("Relection probabitity:%f" %R)
print("Transmittance probabitity:%f" %T)
