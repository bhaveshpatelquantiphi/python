# 4.Write a program to Find the Sum of Digits in a Number

import logging
logging.basicConfig(filename='q2.log',level=logging.DEBUG)
global i
try:
    i = int(raw_input("Enter a Number "))
    if i<0:
        print "Please enter positive number"
    else:
        sum = 0
        j=i
        while (j%10!=0):
            sum += j%10
            j/=10
        print sum
except ValueError: #Handle the exception if unable to convert to int
    print 'Please enter an integer'
    logging.warning(ValueError)
