from logo import logo
import os

print(logo)
print("Welcome to the secret aution programme")

bidders = {}
while True:
    name = input("What is your name? " )
    bid_amount = int(input("What's your bid? "))
    more =  input("Are there any more bidders? Yes or No? ").lower()
    bidders[name] = bid_amount
    
    if more == "yes":
        os.system('cls')
        continue
    elif more == "no":
        max_value = max(bidders.values())
        max_key = max(bidders, key=bidders.get).capitalize()
        print(f"The highest bidder is {max_key} with a bid of {max_value}.")
        break
    else:
        print("Please enter yes or no")
        continue