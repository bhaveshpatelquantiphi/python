# 9.Write a PYTHON program to check the validity of a password chosen by a user.

# To be considered valid, a password
	# a) contains at least 1 letter between [A-Z],
	# b) contains at least 1 letter between [a-z],
	# c) contains at least 1 number between [0-9],
	# d) contains at least 1 special character from [$#@],
	# e) has a minimum length of 6 characters, and
	# f) has a maximum length of 12 characters.

# Your program will consist of two user-defined functions: validate(s) and main().
# The validate() function implements the validation procedure described above. 
# The parameter (or input) to the function is a string s. If s fits the above criteria, print valid. Otherwise, print not valid.


import re

def validate(p):	
	x = True
	while x:  
	    if (len(p)<6 or len(p)>12):
	        break
	    elif not re.search("[a-z]",p):
	        break
	    elif not re.search("[A-Z]",p):
	        break
	    elif not re.search("[$#@]",p):
	        break
	    elif not re.search("[0-9]",p):
	        break
	    else:
	        return ("Valid")
	if(x):
		return "Not Valid"


print validate(raw_input())