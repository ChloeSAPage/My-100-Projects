from logo import logo
import os

bidders = []
print(logo)
print("Welcome to the secret aution programme")

while True:
    name = input("What is your name? " )
    bid_amount = input("What's your bid? ")
    more =  input("Are there any more bidders? Yes or No? ").lower()
    new_bidder = {}
    new_bidder["name"] = name
    new_bidder["bid"] = bid_amount
    bidders.append(new_bidder)
    print(bidders)
    
    if more == "yes":
        #os.system('cls')
        continue
    if more == "no":
        break