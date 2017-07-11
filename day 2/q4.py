# 4. Write a Python program to get the Fibonacci series between 0 to 50
a=0
b=1
k=a+b
print "0"
print "1"
while (b+k+a<50):
	a=b
	b=k
	k=a+b
	print k