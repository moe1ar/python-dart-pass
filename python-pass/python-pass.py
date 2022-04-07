def EVEN_ODD():
	n=int(input("Enter the x value :"))
	num=[]
	for i in range (n):
		number=int(input())
		num.append(number)
	for i in num:
		if 0<i<=10:
			if i%2==0:
				print(i, " is even")
			elif i%2!=0:
				print(i," is odd ")
			else:
				print(" is zero")
		else:
			print(i ,"is out the range ")
EVEN_ODD()
