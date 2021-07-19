array=[1,2,3,4,5]
searchnum = int(input())
flag=0

for i in range(len(array)):
	if(array[i] == searchnum):
		index=i
		flag=1


if(flag == 0):
	print("not found")
else:	
	print(index)		