# 7.Write a program to display an user-defined Exception

class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueNegative(Error):
   """Raised when the input value is negative number"""
   pass

try:
	a = int(input("Enter the positive number : "))
	if a < 0:
		raise ValueNegative

except ValueNegative:
	print "Please enter the positive number"

except ValueError,NameError:
	print "Please enter a valid positive number"