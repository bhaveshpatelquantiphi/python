# 18.Write a Program to Append, Delete and Display Elements of a List Using Classes

class ListClass:
	def __init__(self,l):
		self.l = l	

	def append(self,x): 
		return self.l.append(x)

	def delete(self,x): 
		return self.l.remove(x)

	def display(self): 
		return self.l


lis = ListClass([2,5,5,6,7,9])
lis.append(10)
lis.delete(6)
print lis.display()