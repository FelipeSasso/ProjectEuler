"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""

__author__ = "Felipe Sasso"

def maxprimefactor(n):
	curFactor = 2
	maxFactor = 2

	while n != 1:
		if n % curFactor == 0:
			if curFactor > maxFactor:
				maxFactor = curFactor
			n = n / curFactor
		else:
			curFactor += 1
	return maxFactor

print maxprimefactor(600851475143)
