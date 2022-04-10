def EVEN_ODD():
	n=int(input("Enter the x value :"))
	num=[]
	for i in range (n):
                if 0<i<=10:
			number=int(input())
			num.append(number)
		else:
			print(i ,"is out the range ")
	for i in num:
		
		if i%2==0:
			print(i, " is even")
		elif i%2!=0:
			print(i," is odd ")
		else:
			print(" is zero")
	
EVEN_ODD()
