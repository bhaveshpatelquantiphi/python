# 21.Write a Program to Read the Contents of a File in Reverse Order
for line in reversed(list(open("sample.txt"))):
    print(line.rstrip())