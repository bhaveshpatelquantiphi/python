# 14. Write a Python program to get next day of a given date. 

# Expected Output:
# Input a year: 2016                                                      
# Input a month [1-12]: 08                                                
# Input a day [1-31]: 23                                                  
# The next date is [yyyy-mm-dd] 2016-8-24

import datetime

try:
	date = datetime.datetime(int(raw_input("Enter year : ")), int(raw_input("Enter month number : ")), int(raw_input("Enter date : ")))
	print (date + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
except ValueError as e:
	print e