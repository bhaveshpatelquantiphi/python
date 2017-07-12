def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def mul(x,y):
	return x*y

def div(x,y):
	if y==0:
		return "Can't divide by 0"
	return x/y

def mod(x,y):
	if y==0:
		return "Can't divide by 0"
	if y<0:
		return "Can't be negative"
	return x%int(y)

def input():
	print "Enter first numbers :",
	global a
	a = float(raw_input())
	print "Enter second numbers :",
	global b
	b = float(raw_input())

flag = True
while (flag) :

	input()
	print "Enter your operation :\n + : Plus, - : Minus, * : Multiple, / : Divide, % : Mod, e : Exit\n",
	p = raw_input()

	if(p=='+'):
		print add(a,b)
	
	elif(p=='-'):
		print sub(a,b)

	elif(p=='*'):
		print mul(a,b)

	elif(p=='/'):
		print div(a,b)

	elif(p=='%'):
		print mod(a,b)

	elif(p=='e'):
		flag = False;

	else:
		print "Try again !"