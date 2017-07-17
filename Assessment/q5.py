# 5.Write a Python program to find a missing number from a list
# Input : [1,2,3,4,6,7,8]
# Output : 5

l = [1,2,3,4,6,7,8]

for i in range(min(l),max(l)):
	if i not in l: 
		print i