# 14.Write a Python program to check if a given positive integer is a power of two

x = int(raw_input("Enter a positive number : "))
flag = False
while (True):
	if (x%2 == 0):
		if x==2:
			break;
		flag = True
		x/=2
		print x
	else:
		print "not a power of two"
		flag = False
		break;

if(flag):
	print "Power of two"