a= "Float Calculator"
print(a.center(80)) 

x=float(input("Enter your first number: \n"))
y=float(input("Enter your second number: \n"))
z=input("Choose the operation from the following:\n Add, Sub, Div, Mul, Exp: \n")
if(z=="Add"):
    print(x+y)
elif(z=="Sub"):
    print(x-y)
elif(z=="Div"):
    print(x/y)
elif(z=="Mul"):
    print(x*y)
elif(z=="Exp"):
    print(x**y)
else:
    print("You didn't choose a valid operation")