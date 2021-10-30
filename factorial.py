#!/usr/bin/env python3
# gives the factorial of a number 

print("Enter a number and I'll tell you it's factorial:")
N = int(input())
i = N - 1
n = N
while i > 1:
	n = n * i
	i = i - 1
original = str(N)
factorial = str(n)
print("The factorial of " + str(N) + " is " + str(n))
