import random


# Check cards
def check_user_cards(user_cards, dealer_cards):
    while True:
        if sum(user_cards) > 21:
            if 11 in user_cards:
                for index, card in enumerate(user_cards):
                    if card == 11:
                        user_cards[index] = 1
                        continue
            #   replace with 1
            # check if still over 21
            else:
                print(f"You:{user_cards}")
                print(f"Dealer:{dealer_cards}")
                print("You went bust! You lose!")
                return True

        elif sum(user_cards) == 21:
            print(f"You:{user_cards}")
            print(f"Dealer:{dealer_cards}")
            print("You got 21! You win!")
            return True
        else:
            return False

def check_dealer_cards(user_cards, dealer_cards):
    while True:
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
                if 11 in dealer_cards:
                    for index, card in enumerate(dealer_cards):
                        if card == 11:
                            dealer_cards[index] = 1
                            continue
                else:
                    print(f"You:{user_cards}")
                    print(f"Dealer:{dealer_cards}")
                    print("Dealer went bust! You win!")
                    break
            
            elif sum(dealer_cards) == 21:
                print(f"You:{user_cards}")
                print(f"Dealer:{dealer_cards}")
                print("Dealer got 21! You lose!")
                break

# Draw Cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = random.choices(cards, k=2)
dealer_cards =  random.choices(cards, k=2)
# Display Cards
print(f"You {user_cards}")
print(f"Dealers [{dealer_cards[0]}, ?]")

result = check_user_cards(user_cards, dealer_cards)


# Game
while result == False:
    answer = input("Draw another card? Y/N ").lower().strip()

    if answer == "y":
        user_cards.append(random.choice(cards))
        print(user_cards)
        pass

    result = check_user_cards(user_cards, dealer_cards)

    if result == True:
        break

    if answer == "n":
        check_dealer_cards(user_cards, dealer_cards)
        break