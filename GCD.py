def GCD(x,y):
	if(x<y):
		limit=x
	else:
		limit=y
	for i in range(1,limit+1):
		if(x%i == 0 and y%i == 0):
			gcd = i		
	return gcd



x,y=input("Enter two nums : ").split()
x=int(x)
y=int(y)
gcd = GCD(x,y)
print(gcd)