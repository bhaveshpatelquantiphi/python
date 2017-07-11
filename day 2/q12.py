# 12. Write a Python program to calculate a dog's age in dog's years.
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Input a dog's age in human years: 15                                    
# The dog's age in dog's years is 73

print("Input a dog's age in human years:")
x = int(raw_input())
print "The dog's age in dog's years is" 
ans=0
if x>=2:
	ans = 10.5*2
	ans += (x-2)*4
	print ans
else:
	ans = 10.5*x
	print ans