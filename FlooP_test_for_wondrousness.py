#!/usr/bin/env python3
# Test to see if a number 'N' is wonderous

# if the input 'N' is wondrous, the program halts and gives the answer 'YES'
# if the input 'N' is unwondrous, but causes a closed cycle other than 1-4-2-1-4-2-1, the program halts and gives the answer 'NO' (this doesn't make sense to me)
# if the input 'N' is unwonderous, and causes an endlessly rising progession, the program enver halts.

print("Enter the number you think may be wondrous:")
N = int(input())
remainder = N%1
if remainder == 0 and N >= 0:
	n = N
	i = 0
	while n != 1:
		r = n % 2
		if r == 1:
			n = n * 3 + 1
			print("times 3 plus 1 equals " + str(n))
		elif r == 0:
			n = n / 2
			print("divided by 2 equals " + str(n))
		else:
			print("ERROR")
		i = i + 1
	print("YES! the number " + str(N) + " was found to be wondrous after performing " + str(i) + " operations")
	print("thank you for asking!")
else:
	print("it's not gonna be wondrous if it's not a positive whole number")
