print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

right_left = input(
    "You approach a path, it forks in two directions, which way do you choose? Left or Right? ").lower()
if not right_left == "left":
    print("You fall into a hole. Game Over")
if right_left == "left":
    swim_wait = input(
        "You approach a river, do you swim across or wait for a boat? ").lower()
    if not swim_wait == "wait":
        print("You get wet and soggy, you don't like it and you go home. Game Over.")
    if swim_wait == "wait":
        which_door = input(
            "You approach a number of doors, they have different colours. Which colour door do you enter? Red, Blue, Yellow? ").lower()
        if which_door == "red":
            print("You fall and drown in ketchup. Game Over.")
        elif which_door == "blue":
            print(
                "There is a bouncy castle here, not the treasure you were looking for but fun. Game Over")
        elif which_door == "Yellow":
            print("Congratulations! The treasure is here! You're rich!")
        else:
            print("You just stand there, not choosing, you get nothing. Game Over")
