"""
2.Write a program to demonstrate printing pattern of alphabets

A 
B C 
D E F 
G H I J 
K L M N O 
"""
import logging
logging.basicConfig(filename='q2.log',level=logging.DEBUG)

ch = ord('A') # Getting Ascii of Char 'A'
for x in range(1,6):
    for y in range(x):
        print chr(ch),
        logging.info(ch)
        ch+=1 #increasing the ascii value
    print ""