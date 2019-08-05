print("enter three numbers:")
 
a = int(input())
b = int(input())
c = int(input())
 
if a>b and a>c:
	print(a,"largest")
elif b>a and b>c:
	print(b,"largest")
else:
	print(c,"largest")
