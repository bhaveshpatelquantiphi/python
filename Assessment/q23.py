# 23.Write a Program to Read a String from the User and Append it into a File
f = open("q23.txt","a+")
f.write(raw_input())
print "String Appended"
f.close()