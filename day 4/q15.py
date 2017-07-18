# 15.
# Write a program to solve a classic ancient Chinese puzzle: 
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have?
r = (94-35*2)/2
print("Number of rabbits are  : " + str(r))
print("Number of Chickend are  : " + str(35-r))