def  add(a, b):
       """" This function adds two number"""
       return a+b
def  subtract (a, b):
       """" This function subtract two number """
       return a-b
def multiply (a, b):
      """"This function multiply two number"""
      return a*b
def divide(a, b):
      """''This function divide two number"""
      return a/b
a=int(input ("enter first number : "))
print("Add Operation")
print("1=add")
print("2=subtract")
print("3=multiply")
print("4=divide")
choice=(input ("enter choice 1/2/3/4 : "))
b=int(input ("enter second number : "))
if  choice =="1":
   print (a," +",b,"=",add(a,b))
elif choice =="2":
      print (a," -",b,"=",subtract(a,b))
elif choice =="3":
      print (a,"*",b,"=",multiply(a,b))
elif choice =="4":
     print (a," /",b,"=",divide(a,b))
else:
      print("invalid")
      