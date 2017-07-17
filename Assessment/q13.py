# 13.Write a Python program where you take any positive integer n,
# if n is even, divide it by 2 to get n / 2. 
# If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process until you reach 1.
# Example :
# For instance, starting with n = 12, one gets the sequence 12, 6, 3, 10, 5, 16, 8, 4, 2, 1.
# n = 19, for example, takes longer to reach 1: 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.

i = int(raw_input("Enter a positive number : "))

while i>1:
	print i,
	if i%2 == 0:
		i/=2
	else:
		i= 3*i+1
if i==1:
	print i,
