days =['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
month_lst = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']

print "Enter name of a day ",
p = raw_input()
if p.upper() not in days:
	print "Try again !"
else:
	num = days.index(p.upper());
	print (num+1),
	print " day number of a week" ;

print "Enter month of a day ",
p = raw_input()
if p.upper() not in month_lst:
	print "Try again !"
else:
	num = month_lst.index(p.upper());
	print (num+1),
	print " month number of a year" ;