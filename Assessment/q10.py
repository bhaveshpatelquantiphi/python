# 10.Write a program to accept Date & Time in IST format and convert it to US format(EST).
import datetime

try:
	date = datetime.datetime(int(raw_input("Enter year : ")), int(raw_input("Enter month number : ")), int(raw_input("Enter date : ")),int(raw_input("Enter HOUR : ")),int(raw_input("Enter Minute : ")),int(raw_input("Enter second : ")))
	print datetime.time(9,30,00)
except ValueError as e:
	print e