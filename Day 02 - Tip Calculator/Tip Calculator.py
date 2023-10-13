print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? £"))
num_people = float(input("How many people do you wish to split the bill with? "))
tip = float(input("what percentage tip would you like to give? 10, 12, or 15? "))

tip_percent = tip/100
bill_tip = bill * tip_percent
total_bill = bill + bill_tip
answer = round(total_bill/num_people, 1)
print(f"Each person should pay: £{answer}")