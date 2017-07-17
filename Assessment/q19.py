# 19.Write a Program to Create a Class in which One Method Accepts a String from the User and Another Prints it

class StringClass:
	def __init__(self):
		self.s = ""	

	def input(self):
		self.str = str(raw_input("Enter the string : "))

	def display(self): 
		return self.str

s = StringClass()
s.input()
print s.display()