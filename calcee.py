operator = input("Enter an Operator(+-*/%)")
num1 = float (input ("Enter 1st number: "))
num2 = float (input ("Enter 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(f"{result}  is the required answer")
elif operator == "-":
    result = num1 - num2
    print(f"{result}  is the required answer")
elif operator == "*":
    result = num1 * num2
    print(f"{result}  is the required answer")
elif operator == "/":
    result =  num1 / num2
    print(f"{result}  is the required answer")
elif operator =="%":
    result = num1 % num2
    print(f"{result}  is the required answer")
else :print(f"{operator} is not a valid operator")  