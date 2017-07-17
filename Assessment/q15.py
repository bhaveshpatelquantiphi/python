# 15.Write a program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple
# Example
# Case 1:
# Enter a list of tuples:[(2,5),(1,2),(4,4),(2,3)]
# Sorted:
# [(1, 2), (2, 3), (4, 4), (2, 5)]
 
# Case 2:
# Enter a list of tuples:[(23,45),(25,44),(89,40)]
# Sorted:
# [(89, 40), (25, 44), (23, 45)]

tuple_list = [(1, 2), (2, 3), (4, 4), (2, 5)]
# tuple_list = [(89, 40), (25, 44), (23, 45)]
print(sorted(tuple_list,key=lambda x:x[1]))