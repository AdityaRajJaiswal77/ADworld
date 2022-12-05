print("AD THE BLACK WORLD")
z=True
while z==True: 
         input("NEW CALCULATION")
         choice=(input ("choose +/-/×/÷/**/√/CI/SI  : "))
         if choice ==("√"):
             a=int(input("Enter value  :- "))
             b=a**0.5
             c=int(b)
             print("Square root of",a,"=",c)
             if a != (c*c):
             	 print("It is not a perfect square number")
         elif choice ==("CI"):
          	p=int(input("Enter principal amount : "))
          	r=int(input("Enter rate of intrest : "))
          	t=int(input("Enter time in years : "))
          	A=p*((1+r/100)**t)-p
          	print(A)
         elif choice ==("SI"):
          	p=int(input("Enter principal amount : "))
          	r=int(input("Enter rate of intrest : "))
          	t=int(input("Enter time in years : "))
          	A=p*r*t/100
          	print(A)
         elif choice ==("**"):
          	a=int(input("Enter number :- "))
          	b=int(input("Enter power :- "))
          	print(a,"**",b,"=",a**b)
          	ans=a**b
         else:
               a=int(input("enter first number : "))   
               b=int(input("enter second number : "))
         if  choice ==("+"):
            print(a,"+",b,"=",a+b)
            ans=a+b
         elif choice ==("-"):
             print(a,"-",b,"=",a-b)
             ans=a-b
         elif choice ==("×"):
             print(a,"*",b,"=",a*b)
             ans=a*b
         elif choice ==("÷"):
             print(a,"/",b,"=",a/b)   
             ans=a/b    
         d=input("Do you want to restart your calculation (=/c ) : ")
         if d==("="):
            continue
         elif d==("c"):
             exit()
            
       
             
          