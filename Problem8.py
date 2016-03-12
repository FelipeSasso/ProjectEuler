"""
Problem 8

The four adjacent digits in the 1000-digit number that have the greatest product are 9 * 9 * 8 * 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

"""

def greatestproduct(filename):
	
	a = open(filename)	
	b = a.read()

	greatest = 0;
	for i in xrange(len(b) - 13):
		multi = 1;
		for j in xrange(i, i + 13, 1):			
			multi *= int(b[j])
		if multi > greatest:
			greatest = multi

	a.close()
	return greatest;	
	
print greatestproduct("Problem8.txt")
