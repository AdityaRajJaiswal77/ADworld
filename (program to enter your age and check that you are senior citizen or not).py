#(program to enter your age and check that you are senior citizen or not)
c=True
while c==True:
         a=input("Enter your name = ")
         b=int(input("Enter your age = "))
         if (b>=60):
           print(a,"you are senior citizen")
         elif (b<60):
             print(a,"you are not senior citizen")
         d=input("Do you want to repeat yes/no??? = ")
         if d==("yes"):
            continue
         else:
             exit()
         
