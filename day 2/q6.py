# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 7, 7;
Matrix = [[0 for x in range(w)] for y in range(h)] 
# Matrix=[[1, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0, 0]]
Matrix=[[0, 0, 1, 1, 1, 0, 0],[0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 0, 0, 1]]
print("\n\n"),

for x in range(0,7):
	for y in range(0,7):
		if(Matrix[x][y]==1):
			print("* "),
		else:
			print("  "),
	print('\n')