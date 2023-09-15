import os

def add(first_num, second_num):
    result = first_num + second_num
    return result

def subract(first_num, second_num):
    result = first_num - second_num
    return result

def multiply(first_num, second_num):
    result = first_num * second_num
    return result

def divide(first_num, second_num):
    result = first_num / second_num
    return result

while True:
    first_num = input("What is the first number? ")
    operation = input("Pick an operator\n+\n-\n*\n/\n")
    second_num = input("What is the second number? ")

    if operation == "+":
        add(first_num, second_num)
    elif operation == "-":
        subract(first_num, second_num)
    elif operation == "*":
        multiply(first_num, second_num)
    elif operation == "/":
        multiply(first_num, second_num)

    yes_no = input("Exit or new calc").lower()
    if yes_no == "exit":
        break
    elif yes_no == "n":
        os.system('cls')
        continue