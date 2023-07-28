import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# 1 beats 3
# 3 beats 2
# 2 beats 1
user_choice = int(input("Choose 1 for Rock, 2 for Paper or 3 for Scissors "))

computer_choice = random.randint(1 , 3)

# The game

if user_choice == computer_choice:
    print("Draw!")

elif user_choice == 1 and computer_choice == 3:
    print("You win!")

elif user_choice > computer_choice:
    print("You win!")

elif user_choice > 3:
    print("You can choose that number")
else:
    print("You lose!")

print(f"computer = {computer_choice} you = {user_choice}")
