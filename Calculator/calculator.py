def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def subtract(a ,b):
    return a - b

operators = {"+" : add, "*" : multiply, "/" : divide, "-" : subtract}

num1 = int(input("Enter the first number: "))
for key in operators:
    print(key)
operator = input("Pick an operation from the line above: ")
num2 = int(input("Enter the second number: "))

equation = operators[operator]
answer = equation(num1,num2)

print(f"{num1} {operator} {num2} = {answer}")