# Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
print("Enter the number : ")
i = int(raw_input())
j = 1

while j<=i:
	print "* "*j
	j+=1


j=i-1
while j>0:
	print "* "*j
	j+=-1