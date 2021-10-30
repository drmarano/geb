#!/usr/bin/env python3
# Calculates Pi to a certain number of decimal places.

print("What digit of pi do you want to know?")
N = input()
N = int(N)
if N >= 0:
	n = 10**(N+2)
	pi = 0.0
	i = 0
	while i <= n:
		print(pi)
		pi = pi + ((4.0*((-1.0)**i))/(1.0+2.0*i))
		i = i + 1
print("equals " + str(pi))

