import math

array=[11,22,33,44,55,66]
low=0
high=len(array)-1
searchnum=int(input("Enter num: "))
temp=0

while(low<=high):
	
	middle=math.ceil((low+high)/2)
	if(middle == temp):
		print("not found")
		break
	if(array[middle]==searchnum):
		print(middle)
		break
	elif(array[middle] < searchnum):
		low=middle
		temp=middle
	elif(array[middle] > searchnum):
		high=middle
		temp=middle
	

