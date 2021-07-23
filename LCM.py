def GCD(x,y):
	if(x<y):
		limit=x
	else:
		limit=y
	for i in range(1,limit+1):
		if(x%i == 0 and y%i == 0):
			gcd = i		
	return gcd


def LCM(x,y):
	gcd = GCD(x,y)
	return (x*y)//gcd



x,y,z=input("Enter three nums : ").split()
x=int(x)
y=int(y)
z=int(z)
Lcm = LCM(x,LCM(y,z))	
print(Lcm)

str="mani"
new = str
print(new + 5)
