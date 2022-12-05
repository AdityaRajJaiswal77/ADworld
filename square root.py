# (AD The Black World)
# Python program for finding square root 
z=True
while z==True:	
    a=int(input("Enter value  :- "))
    b=a**0.5
    c=int(b)
    print("Square root of",a,"=",c)
    if a != (c*c):
    	print("It is not a perfect square number")
    d=input("Do you want to repeat (=|c)  :- ")
    if d==("="):
    	continue
    elif d==("c"):
    	exit()

    
    
    