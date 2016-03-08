__author__ = "Felipe Sasso"

def fib(n):
	if n < 2:
		return n
	else:
		return fib(n - 1) + fib(n - 2)

sum = 0
term = 1
curterm = 0
while curterm < 4000000:
	curterm = fib(term);
	if(curterm % 2 == 0):
		sum+= curterm
	term += 1

print sum
