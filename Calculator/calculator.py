num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))

print("Choose operator:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

operator = int(input("Enter operator number:"))

if(operator in {1,2,3,4}):
    if(operator == 1):
        result=num1+num2
    elif(operator == 2):
        result=num1-num2    
    elif(operator == 3):
        result=num1*num2    
    elif(operator == 4):
        if (num2==0):
            result = None
            print ("Invalid, Cannot divide by zero")
        else:
            result=num1/num2
else:
    print("Invalid operator number entered")

print("Result of the operation is: ", result)
