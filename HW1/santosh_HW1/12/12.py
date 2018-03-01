#Recursion
print("ANSWER TO PART A")
def catalan(n):
    if n==0:
        return 1
    else:
        c_n=((4*n-2)*catalan(n-1))/(n+1)
    return c_n

n=input("Catalan number: enter the value of n:")
n=int(n)
c_n=catalan(n)

print("Answer:%d" %(c_n))

print("ANSWER TO PART B")
def gcd(m,n):
    if n==0:
        return m
    else:
        r=m%n
        ans=gcd(n,r)
    return ans

m=input("GCD:: enter m:")
n=input("enter n:")
m=int(m)
n=int(n)
print("The gcd of two number is : %d" %(gcd(m,n)))
