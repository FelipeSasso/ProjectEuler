"
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"

__author__ = "Felipe Sasso"

def largestpalindromeproduct():
	largest = 0
	for i in xrange(999, 100, -1):
		for j in xrange(999, 100, -1):
			x = i * j
			if str(x) == str(x)[::-1]:
				if x > largest:
					largest = x
	return largest

print largestpalindromeproduct()
