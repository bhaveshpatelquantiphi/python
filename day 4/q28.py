# 28. 
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

import re
p = raw_input("A sequence of comma separated passwords ")
pas = p.split(",")
print "Valid passwords are :",
for a in pas:
	x = True
	while x:  
	    if (len(a)<6 and len(a)>12):
	        break
	    elif not re.search("[a-z]",a):
	        break
	    elif not re.search("[0-9]",a):
	    	break
	    elif re.search(" ",a):
	        break
	    elif not re.search("[A-Z]",a):
	        break
	    elif not re.search("[$#@]",a):
	        break
	    else:
	        print a,
	        x=False
	        break