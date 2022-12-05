# (AD The Black World)
# python program for checking prime number
a=int(input("Enter your no.= "))
if a>1:
	for i in range (2,a):
		if (a % i)==0:
			print(a,"No it is not prime number")
			break
	else:
		print(a,"Yes it is prime number")
else:
		print(a,"No it is not prime number")
		exit()

		
			
	