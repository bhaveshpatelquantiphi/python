# 17.Please write a program which accepts a string from console and print the characters that have even indexes.

# Example:
# If the following string is given as input to the program:
# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be:
# Helloworld
import sys
t=""
for x in range(0,len(sys.argv[1]),2):
	t+=sys.argv[1][x]
print t