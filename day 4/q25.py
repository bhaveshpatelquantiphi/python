# 25.Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# google

str = "john@google.com"

print str[str.index("@")+1:str.index(".")]