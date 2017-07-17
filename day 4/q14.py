# 14. Write a Python program to get next day of a given date. 

# Expected Output:
# Input a year: 2016                                                      
# Input a month [1-12]: 08                                                
# Input a day [1-31]: 23                                                  
# The next date is [yyyy-mm-dd] 2016-8-24


import datetime as dt
today = dt.now()
date_string = dt.strftime(today, '%m/%d/%Y')
print(date_string) 