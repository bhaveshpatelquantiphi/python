# 11.Write a Python program to find whether it contains an additive sequence or not.
# The additive sequence is a sequence of numbers where the sum of the first two numbers is equal to the third one.
# Sample additive sequence: 6, 6, 12, 18, 30
# In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
# Also, you can split a number into one or more digits to create an additive sequence.
# Sample additive sequence: 66121830
# In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
# Note : Numbers in the additive sequence cannot have leading zeros.


seq = [6,6,12,18,30,48,78]
flag =False

for x in range(0,len(seq)-2):
	if seq[x]+seq[x+1]==seq[x+2]:
		flag = True
	else:
		flag = False
		print "Not a valid sequence"

if flag:
	print "Valid Sequence"