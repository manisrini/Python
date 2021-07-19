# str1 = (input())
# first = chr(ord(str1[0])-32)
# last = chr(ord(str1[-1])-32)

# newstr = first + str1[1:len(str1)-1] + last
# print(newstr)
# count=0

# for word in newstr:
# 	if(word!=' '):
# 		count = count+1
# print(count)		



class dog:
	

	def __init__(self,name):
		self.name = name

	def getName(self):
		return self.name	

ob1 = dog("m")
print(ob1.getName())	