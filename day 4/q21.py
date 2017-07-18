# 21.With a given list [12,24,35,24,88,120,155,88,120,155],
# write a program to print this list after removing all duplicate values with original  order reserved.

input = [12,35,24,88,120,24,155,88,120,155]
output = []
for x in input:
	if x not in output:
		output.append(x)
print output