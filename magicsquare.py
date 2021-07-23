size = int(input("Enter the matrix size: "))
magic_square = []

for i in range(size):
	a=[]
	for j in range(size):
		a.append(int(input('Enter arr[%d][%d] : ' %(i,j))))
	magic_square.append(a)	


rowsum,colsum=0,0
row,col=[],[]

for i in range(size):
	for j in range(size):

		
		rowsum = rowsum + magic_square[i][j]
		colsum = colsum + magic_square[j][i]
		
	row.append(rowsum)
	col.append(colsum)
	rowsum=0
	colsum=0

			


if(len(set(row))!= 1 or len(set(col))!=1):
	print("Not a magic square !!!")
	exit()

if(row == col):
	print("A magic square!!!")	



					

