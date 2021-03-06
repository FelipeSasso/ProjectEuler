"""
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 2^5 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
__author__ = "Felipe Sasso"

def istriplet(a, b, c):
	if a**2 + b**2 == c**2:
		return True
	return False

def triplet():
		for b in range(998, 0, -1):
			for a in range(997, 0, -1):
				c = 1000 - (a + b)
				if istriplet(a, b, c):
					return a * b * c

print triplet()
