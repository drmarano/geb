# gives the factorial of a number 


print "Enter two whole numbers and I'll tell you the remainder of Num1/Num2:"
print "Enter Num1:"
M = input()
print "Enter Num2:"
N = input()
if M >= N and ( type(N) == long or type(N) == int ) and ( type(M) == long or type(M) == int ):
	R = M - N
	while R >= N:
		R = R - N
	print "The remainder of " + str(M) + "/" + str(N) + " is " + str(R)
else:
	print "bad nums bub"

