"""Calculating Derivatives."""


def funct(x):
    f = x * (x - 1)
    return f

def Derivatives(x , delta):
    df = funct(x+delta) - funct(x)
    der = df/delta
    return der

def result(delta):
    print("The dervative at x=1 with  delta =%f is :: %f" %(delta,Derivatives(x,delta)))




x = input("Enter x :")
x = float(x)
print("The functional value: %f" %(funct(x)))
result(1e-2)
result(1e-4)
result(1e-6)
result(1e-8)
result(1e-10)
result(1e-12)
result(1e-14)

