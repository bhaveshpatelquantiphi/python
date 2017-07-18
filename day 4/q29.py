# 29.Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
print "D means deposit while W means withdrawal.\n Suppose the following input is supplied to the program:\n D 300\n D 300\n W 200\n D 100\n"
l = []
a = []
for x in range(0,int(input("Enter the number of trasaction\n"))):
	i = raw_input()
	j= i.split(" ")
	l.append(j[0])
	a.append(int(j[1]))
sum=0
for x in range(len(l)):
	if(l[x]=='D'):
		sum+=a[x]
	else:
		sum-=a[x]

print "Total amount is "+ str(sum)
