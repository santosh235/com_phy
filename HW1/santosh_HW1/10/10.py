#BINOMIAL COEFFIECIENTS
print("\t ANSWER TO PART a::")
def factorial(x):
	ans=1
	for i in range(1,x+1):
		ans=ans*i
	return ans


def binomial(n,k):
	if k==0:
		return 1
	
	result=int(factorial(n)/(factorial(k)*factorial(n-k)))
	return result

n=input("Enter the value of n :: ")
k=input("Enter the value of k :: ")
n=int(n)
k=int(k)
if n<k:
	print("n should be greater than k")
else:
	ans=binomial(n,k)
	print("Ans::"+str(ans))

#Pascal triangle

print("\n\t ANSWER TO PART b")
print("The first 20 lines of pascal triangle:")

for n in range(1,21):
	for i in range(0,n+1):
		num=binomial(n,i)
		print(num,end=' ')	
	print("\n")

#Probability

print("ANSWER TO PART c::")
prob_1=binomial(100,60)/(2**100)
print("The probability to get exactly 60 heads :"+str(prob_1))
prob_2=0
for i in range(60,101):
	prob_2=prob_2+binomial(100,i)/(2**100)
print("The probability to get 60 heads and above :"+str(prob_2))

