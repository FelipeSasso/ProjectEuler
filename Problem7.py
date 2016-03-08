"""
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

"""
__author__ = "Felipe Sasso"

def isprime(n):
	
	for i in xrange(1, n):
		if n % i == 0 and i != 1 and i != n:
			return False
		
	return True

def countprimes(n):
	
	count = 1
	
	while True:
		for i in xrange(3, 999999999, 2 ):
			if isprime(i):
				count +=1
				if count == n:
					return i


print countprimes(10001)
