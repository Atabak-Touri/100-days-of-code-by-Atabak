print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island."
      "Your mission is to find the treasure.")
path=input("which way you want to go? left or right?\n")
swim=input("do you want to swim or wait?\n")
door=input("which door you will choose? red, yellow or blue?\n")

if path == "right" and "Right":
    print("Fall into a hole."
          "Game Over.")
elif swim == "swim" and "Swim":
    print("Atacked by a trout."
          "Game Over")
if swim=="wait" and "Wait":

elif door == "Blue" and "blue":
        print("eaten by beasts Game Over.")
    elif door== "Red" and "red":
        print("burned by fire. game over")
    elif door=="Yellow" and "yellow":
        print("You Win!")
else:
    print("game over")

# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# first_way= input("choose a way? left or right?")
# second_way= input("which way you would choose? swim or wait?")
# third_way= input("choose the way? red, blue or yellow?")
# if first_way == "right":
#     print("game over")
# elif second_way == "swim" :
#     print("game over")
# elif third_way == "yellow":
#     print("You WIN!")
# elif third_way == "blue":
#     print("Eaten by beasts. game over.")
# elif third_way== "red":
#     print("burned by fire. game over.")
# else:
#     print("game over")