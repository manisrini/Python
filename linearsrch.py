array=[]
size = int(input('Enter array size : '))
for i in range(size):
	inp = int(input("Enter arr[%d] : " %(i)))
	array.append(inp)
searchnum = int(input("Enter num to be searched : "))
flag=0

for i in range(len(array)):
	if(array[i] == searchnum):
		index=i
		flag=1


if(flag == 0):
	print("not found")
else:	
	print("Element found at %d" %index)		