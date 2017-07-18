# 20. Define a class Person and its two child classes: Male and Female. 
# All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person(object):
	"""docstring for Person"""
	def __init__(self):
			pass

class Male(Person):
	"""docstring for Male"""
	def __init__(self):
		pass

	def getGender(self):
		return "Male"

class Female(Person):
	"""docstring for Female"""
	def __init__(self):
		pass
	def getGender(self):
		return "Female"

p1 = Male()
print p1.getGender()

p2 = Female()
print p2.getGender()