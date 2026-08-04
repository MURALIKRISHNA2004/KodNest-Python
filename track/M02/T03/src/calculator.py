num1=int(input("Enter the Number 1 : "))
num2=int(input("Enter the Number 2 : "))
operator=str(input("Enter the Operator : "))
if operator=='+':
    print(f"The result of Addition is {num1+num2}")
elif operator=='-':
    print(f"The result of subtraction is {num1-num2}")
elif operator=='*':
    print(f"The result of Multiplication is {num1*num2}")
elif operator=='/':
    print(f"The result of Division is {num1/num2}")
else:
    print("Invalid Operator")