"""
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

__author__ = "Felipe Sasso"

def isprime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def sumofallprimesbellown(n):

	if n <= 1:
		return 0

	if n == 2:
		return 2
	
	tot = 2
	a = 3
	while a < n:
		if isprime(a):
			tot += a			
		a += 2
	return tot

print sumofallprimesbellown(2000000)
