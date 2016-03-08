"""
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

__author__ = "Felipe Sasso"

def isdivisiblebyall(n):

	for i in range(1, 20):
		if n % i != 0:
			return False
	return True

def smallestmultiple():
	a = 20
	while True:
		if isdivisiblebyall(a):
			return a
		a += 2

print smallestmultiple()
