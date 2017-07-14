import logging
import datetime

# now = datetime.datetime.now()
logging.basicConfig(filename='example.log',level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')

def add(x,y): 
	"""
    add (x(float), y(float))
    Return (float) :addition of first and second number """
	return x+y

def sub(x,y):
    """
    sub (x(float), y(float))
    Return (float) :Subtraction of first and second number 	"""
    return x-y

def mul(x,y):
    """
    mul (x(float), y(float))
    Return (float) :Multiple of first and second number  """
    return x*y

def div(x,y):
    """
    div(first number(float), second number(float))
    Return (float) :Division of first and second number
    """
    try:
        return x/y
    except ZeroDivisionError,e:
        logging.warning("Can't divide by zero"+"\t"+str(x)+"  "+str(y)+"\t"+str(datetime.datetime.now()))
    print "Can't divide by zero"

def mod(x,y):
    """
    Mod(first number(float), second number(float))
    Return (float) :Modulus of first and second number
    """
    if y==0: # If denominator is zero
        # logging.warning('Can\'t divide by zero',x,y)
        return "Can't divide by 0"
    if y<0: # If denominator is Negative
        # logging.warning('Can\'t be negative',x,y)
        return "Can't be negative"
    return x%int(y)

def input():
    """
    Input()
        Common function to take number inputs a,b
    """
    print "Enter first numbers :",
    global a

    try:
        a = float(raw_input())
    except ValueError,e:
        print e

    print "Enter second numbers :",
    global b
    try:
        b = float(raw_input())
    except ValueError,e:
        print ValueError,e


flag = True
while (flag) :
	input()
	print "Enter your operation :\n + : Plus, - : Minus, * : Multiple, / : Divide, % : Mod, e : Exit\n",
	p = raw_input()

	# Compare the input operation and call the operation
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