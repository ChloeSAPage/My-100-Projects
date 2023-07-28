import random

rock = '''Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''Scissors
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
user_choice -= 1
computer_choice = random.randint(0 , 2)

# 0 beats 2
# 2 beats 1
# 1 beats 0

# Showing the ascii art.
list = [rock, paper, scissors]
print(f"You picked: {list[user_choice]}")
print(f"The computer picked: {list[computer_choice]}")

# The game
if user_choice == computer_choice:
    print("Draw!")

elif user_choice == 0 and computer_choice == 2:
    print("You win!")

elif user_choice == 1 and  computer_choice == 0:
    print("You win!")

elif user_choice == 2 and  computer_choice == 1:
    print("You win!")

elif user_choice > 3:
    print("You can't choose that number")

else:
    print("You lose!")

