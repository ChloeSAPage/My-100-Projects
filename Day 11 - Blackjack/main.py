import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_cards = random.choices(cards, k=2)
bot_cards =  random.choices(cards, k=2)
print(sum(user_cards))

answer = input("Ready for your cards? Y/N? ").lower().strip()

while True:
    if answer == "y":
        print(f"You {user_cards}")
        print(f"Dealers [{bot_cards[0]}, ?]")
        break
    if answer == "n":
        exit
    else:
        print("Type Y or N")


answer = input("Do you want another card? Y/N ").lower().strip()
while True:
    if answer == "y":
        break
    if answer == "n":
        user_total = sum(user_cards)
        if user_total > 21:
            print("You lose!")
        break