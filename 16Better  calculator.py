num1 = float(input("Enter a number in decimals"))
op= input("Enter + , - , * ,/, Corresponding to the operation to be performed")
num2 = float(input("Enter the second number"))

if op == "+":
    print("The sum of the two numbers is:",num1+num2)
elif op == "-":
    print("The difference of the two numbers is:",num1-num2)
elif op == "*":
    print("The product of the two numbers is",num1*num2)
elif op == "/":
    print("The quotient is equal to:",num1/num2)
else:
    print("Invalid output")
