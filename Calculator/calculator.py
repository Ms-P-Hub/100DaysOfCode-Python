from art import logo
import os

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def subtract(a, b):
    return a - b

operators = {"+": add, "*": multiply, "/": divide, "-": subtract}


def calculation():
    print(logo)
    again = True
    num1 = float(input("Enter the first number: "))

    while again:
        for key in operators:
            print(key)
        operator = input("Pick an operation from the line above: ")
        num2 = float(input("Enter the next number: "))

        equation = operators[operator]
        answer = equation(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")

        should_continue =input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit s to start a new calculation: ").lower()
        
        if should_continue == "y":
            num1 = answer
            again = True
        elif should_continue == 's':
            os.system('clear')
            calculation()
        else:
            break
calculation()