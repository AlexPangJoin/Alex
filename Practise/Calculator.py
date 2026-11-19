# Math Calculator

Operator = input("Enter an operator (+, -, *, /): ")
Num1 = float(input("Enter the first number: "))
Num2 = float(input("Enter the second number: "))

if Operator == "+":
    result = Num1 + Num2
    print (round(result,3))
elif Operator == "-":
    result = Num1 + Num2
    print (round(result,3))
elif Operator == "*":
    result = Num1 * Num2
    print (round(result,3))
elif Operator == "/":
    result = Num1 / Num2
    print (round(result,3))
else:
    print("f{Operator} is not a valid operator")

