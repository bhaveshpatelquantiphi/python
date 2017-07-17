# 16.Write a Program to Count the Number of Lines in a Text File
f= open("countlines.txt")
num_lines = sum(1 for l in f)
print num_lines