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
