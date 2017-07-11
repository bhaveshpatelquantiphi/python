print("Enter row number")
n = int(raw_input())
print("Enter column number")
m = int(raw_input())
if(n<3 or m <3 ):
	print "! **Please give row or column value greater than 3**"
else:
	for i in range(0,n):
		for j in range(0,m):
			if(j==0 and i!=n-1):
				print "*",
			if(i==n-1 and i!=0):
				print "*",
		print ""