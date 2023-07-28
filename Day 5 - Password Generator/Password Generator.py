import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

rand_letter = random.randint(0, len(letters)) 
rand_number = random.randint(0, len(numbers))
rand_symbols = random.randint(0, len(symbols))

# Picking

password = []

for index in range(0, nr_letters):
    rand_letter = random.randint(0, len(letters)-1)
    password.append(letters[rand_letter])

for index in range(0, nr_symbols):
    rand_symbols = random.randint(0, len(symbols)-1)
    password.append(symbols[rand_symbols])

for index in range(0, nr_numbers):
    rand_number = random.randint(0, len(numbers)-1)
    password.append(numbers[rand_number])

# Random Order

for number in range(0, 1000):
  random_number1 = random.randint(0, len(password)-1)
  random_number2 = random.randint(0, len(password)-1)
  password[random_number1], password[random_number2] = password[random_number2], password[random_number1]

result_password = ''.join(password)
print(result_password)