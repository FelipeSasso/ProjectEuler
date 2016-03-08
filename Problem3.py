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
