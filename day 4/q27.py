# 27.Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
set = (1,2,3,4,5,6,7,8,9,10)
s=[]
for x in set:
	if(x%2==0):
		s.append(x)
print tuple(s)