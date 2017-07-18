# 22.By using list comprehension,
# please write a program to print the list after 
# removing the v0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
input = [12,24,35,70,88,120,155]
for x in range(0,len(input)-1,2):
	input.remove(input[x])
print input