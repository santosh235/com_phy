#Spaceship travel
import math
def time(x,v):
    t=(31536000*x)/v
    return t

x=input("Enter the distance(in light year):")
v=input("Enter the speed as fraction of v:")
x=float(x)
v=float(v)

t_obs=(time(x,v))/86400.0
gamma_inv=math.sqrt(1-(v*v))
l_cont=x*gamma_inv
t_pass=time(l_cont,v)/86400.0

print("The time in earth's frame: %f days" %(t_obs))
print("The time in passenger's frame: %f days" %(t_pass))
