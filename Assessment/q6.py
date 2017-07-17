# 6.Assuming that we have some email addresses in the "username@companyname.com" format,
# 	please write program to print the user name of a given email address. 
#   Both user names and company names are composed of letters only.


import logging
logging.basicConfig(filename='q6.log',level=logging.DEBUG)

s = raw_input("Enter the Email id : ") #sample input bhavesh.patel@quantiphi.com
try:
	print s[:s.index('@')]				#getting index of '@' char
except ValueError as ve:
	print "ERROR : @ not found"
	logging.warning('ValueError')