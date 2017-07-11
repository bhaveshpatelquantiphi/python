import sys
a = sys.argv[1]
b = a[::-1]
print a[1:5]
if a==b:
	print(a+" is palindrome")
else:
	print(a+" is not a palindrome")