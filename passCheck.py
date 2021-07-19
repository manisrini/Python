
def isValid(password):
	if(len(password) < 8 or len(password) > 15):
		print("Length must be between 8 to 15 characters")
		return False

	if(" " in password):
		print("Space should not be there")
		return False	

	count = 0
	numbers=['0','1','2','3','4','5','6','7','8','9']
	for i in password:
		if i in numbers:
			count =1
	if(count == 0):
		print("Must contain atleast 1 number")
		return False


	count=0
	special=['@','!','#','$','%','^','*','&','(',')','_','-','+','=','{','[','}',']','|',".",'>',',','<','?','/']
	for i in password:
		if i in special:
			count=1
	if(count==0):
		print("Must contain atleast 1 special character")
		return False	


	#lowercase 
	count=0
	for i in range(97,122):
		if(chr(i) in inp):
			count=1

	if(count==0):
		print("Must contain atleast 1 lowercase letter")
		return False

	# uppercase	
	count=0
	for i in range(65,90):
		if(chr(i) in inp):
			count=1

	if(count==0):
		print("Must contain atleast 1 uppercase letter")
		return False
	

	return True
		




# main
inp = input("Enter a string : ")
if(isValid(inp)):
	print("Your password is valid :)")
else:
	print("Your password is invalid :(")		