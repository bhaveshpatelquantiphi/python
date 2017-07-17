# 17.Define a class named Circle which can be constructed by a radius. 
#    The Circle class has a method which can compute the area.

class Circle:
	def __init__(self,radius):
		self.radius = float(radius)	

	def getArea(self): 
		return 3.14*(self.radius**2)

r = int(input("Enter the radius (Float)"))
c = Circle(float(r))
print c.getArea()