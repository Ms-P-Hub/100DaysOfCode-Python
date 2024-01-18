num1 = int(input("Enter the first number: "))
operator = input("Enter the operator: ")
num2 = int(input("Enter the second number: "))

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def subtract(a ,b):
    return a - b

operators = {"+" : add, "*" : multiply, "/" : divide, "-" : subtract}

equation = operators[operator]
answer = equation(num1,num2)

print(f"{num1} {operator} {num2} = {answer}")