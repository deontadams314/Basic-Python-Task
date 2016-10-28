def factorial(n):
	if n < 1: # Base Case
		return 1
	else:
		return n * factorial(n-1) 
