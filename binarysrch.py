import math

array=[]
size = int(input('Enter array size : '))
for i in range(size):
	inp = int(input("Enter arr[%d] : " %(i)))
	array.append(inp)
low=0
high=len(array)-1
searchnum=int(input("Enter num to be searched: "))
temp=0

while(low<=high):
	
	middle=math.ceil((low+high)/2)
	if(middle == temp):
		print("not found")
		break
	if(array[middle]==searchnum):
		print("Element found at index %d " %middle)
		break
	elif(array[middle] < searchnum):
		low=middle
		temp=middle
	elif(array[middle] > searchnum):
		high=middle
		temp=middle
	

