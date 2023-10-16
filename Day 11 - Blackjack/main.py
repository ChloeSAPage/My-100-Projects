import random

# Draw Cards
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_cards = random.choices(cards, k=2)
dealer_cards =  random.choices(cards, k=2)
# Display Cards
print(f"You {user_cards}")
print(sum(user_cards))
print(f"Dealers [{dealer_cards[0]}, ?]")
# Game
while True:
    answer = input("Do you want another card? Y/N ").lower().strip()

    if answer == "y":
        user_cards.append(random.choice(cards))
        print(user_cards)
        print(sum(user_cards))
        pass
    
    if sum(user_cards) < 21 and sum(dealer_cards) > 21:
        print(f"You:{user_cards}")
        print(f"Dealer:{dealer_cards}")
        print("Dealer went bust! You win!")
        break

    elif sum(user_cards) > 21:
        print(f"You:{user_cards}")
        print(f"Dealer:{dealer_cards}")
        print("You went bust! You lose!")
        break

    elif sum(user_cards) == 21 and not sum(dealer_cards) == 21:
        print(f"You:{user_cards}")
        print(f"Dealer:{dealer_cards}")
        print("You win!")
        break

    elif sum(dealer_cards) == 21 and not sum(user_cards) == 21:
        print(f"You:{user_cards}")
        print(f"Dealer:{dealer_cards}")
        print("You lose!")
        break
    
    elif sum(user_cards) == 21 and sum(dealer_cards) == 21:
        print(f"You:{user_cards}")
        print(f"Dealer:{dealer_cards}")
        print("You Draw!")
        break
    
    if answer == "n":
        while True:
            print(f"Dealer: {sum(dealer_cards)}")
            if sum(dealer_cards) < 21:
                if sum(user_cards) > sum(dealer_cards):
                    dealer_cards.append(random.choice(cards))
                    continue
                elif sum(user_cards) < sum(dealer_cards):
                    print(f"You:{user_cards}")
                    print(f"Dealer:{dealer_cards}")
                    print("You lose!")
                    break
                elif sum(user_cards) == sum(dealer_cards):
                    dealer_cards.append(random.choice(cards))

            elif sum(dealer_cards) > 21:
                print(f"You:{user_cards}")
                print(f"Dealer:{dealer_cards}")
                print("Dealer went bust! You win!")
                break
            
            elif sum(dealer_cards) == 21:
                print(f"You:{user_cards}")
                print(f"Dealer:{dealer_cards}")
                print("You lose!")
                break
        break
