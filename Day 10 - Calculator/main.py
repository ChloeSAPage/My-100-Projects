import os


def add(first_num, second_num):
    return first_num + second_num

def subract(first_num, second_num):
    return first_num - second_num

def multiply(first_num, second_num): 
    return first_num * second_num

def divide(first_num, second_num):
    try:
        return first_num / second_num
    except ZeroDivisionError:
        print("You cannot divide a number by 0")

operations = {
    '+': add, 
    '-': subract, 
    '*': multiply, 
    '/': divide
              }

while True: # Handle issue
    try:
        first_num = float(input("What is the first number? "))
        break
    except ValueError:
        print("Enter a valid number")

while True:
    for operation in operations:
        print(operation)

    while True:
        try:
            operation = input("Pick an operator\n")
            calc = operations[operation]
            second_num = float(input("What is the second number? "))
            break
        except ValueError:
            print("Enter a valid number")
            continue
        except KeyError:
            print("Enter a valid operator")
    
    answer = calc(first_num, second_num)
    
    if answer == None:
        print(f"First number is {first_num}")
        continue

    print(f"{first_num} {operation} {second_num} = {answer}")

    yes_no = input(f"Type 'y' to keep calculating with {answer},'n' for a new calculation or 'e' to exit  " ).lower()
    match yes_no: 
        case "e":
            print("Goodbye")
            break
        
        case "n":
            os.system('cls')
            while True:
                try:
                    first_num = float(input("What is the first number? "))
                    break
                except ValueError:
                    print("Enter a valid number")
                    continue
        
        case "y":
            first_num = answer
