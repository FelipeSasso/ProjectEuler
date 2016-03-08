"
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"

__author__ = "Felipe Sasso"

def sumofmultiples(n):
	sum = 0;
	for i in xrange(1, n):
		if (i % 3 == 0) or (i % 5 == 0):
			sum += i
	return sum

print sumofmultiples(1000)
