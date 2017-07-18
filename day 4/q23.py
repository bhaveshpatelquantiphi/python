# 23.Please write a binary search function which searches an item in a sorted list. 
# The function should return the index of element to be searched in the list.


def bsearch(list,l,h,x):
	if h >= l:
		mid = l + (h - l)/2
		if list[mid] == x:
			return mid
		elif list[mid] > x:
			return bsearch(list, l, mid-1, x)
		else:
			return bsearch(list, mid+1, h, x)
	else:
		return -1


l = [12,80,24,35,100,70,88,5,120,155]
l.sort()
print "List : ",
print l
a = bsearch(l,0,len(l)-1,70)
if a !=-1:
	print str(70)+ " found at index " + str(a)
else:
	print " Not Found"