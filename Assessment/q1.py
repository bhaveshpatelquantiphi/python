# 1. Write a program to raise a RunTimeError Exception
import logging
logging.basicConfig(filename='q1.log',level=logging.DEBUG)

try:
	string = int("8OO9")
except Exception:
	print "RunTimeError"
	logging.warning('RunTimeError')