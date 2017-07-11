# Write a Python program to convert temperatures to and from celsius, fahrenheit.
print("Enter the Format of Temperature")
print("1. for Fahrenheit")
print("2. for Celsius")
f = int(raw_input())
if(f==1):
	print("Enter the temperature value")
	tf = float(raw_input())
	print(float((tf-32)*5/9))
elif(f==2):
	print("Enter the temperature value")
	tf = float(raw_input())
	print(float((tf*9/5+32)))
else:
	print "Invalid number"