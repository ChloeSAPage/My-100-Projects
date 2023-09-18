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

operations = {
    '+': add, 
    '-': subract, 
    '*': multiply, 
    '/': divide
              }

first_num = float(input("What is the first number? "))
while True:
    operation = input("+\n-\n*\n/\nPick an operator\n")
    second_num = float(input("What is the second number? "))
    
    calc = operations[operation]
    answer = calc(first_num, second_num)
    
    print(f"{first_num} {operation} {second_num} = {answer}")

    yes_no = input(f"Type 'y' to keep calculating with {answer},'n' for a new calculation or 'e' to exit  " ).lower()
    match yes_no: 
        case "e":
            print("Goodbye")
            break
        
        case "n":
            os.system('cls')
            first_num = int(input("What is the first number? "))
            continue
        
        case "y":
            first_num = answer
