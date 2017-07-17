# 22.Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# a = raw_input("Enter the string")
a = "hello world! 123"
l = 0
d = 0
print a
for x in range(len(a)):
	if(a[x].isdigit()):
		d+=1
	if(a[x].isalpha()):
		l+=1

print "Letters : "+ str(l)
print "Digits  : "+ str(d)