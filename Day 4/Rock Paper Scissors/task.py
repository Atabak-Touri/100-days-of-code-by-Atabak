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
choice=int(input("What do you want to choose? 0 for rock, 1 for paper, 2 for scissors"))
if choice== 0:
    print(f" your coice: {rock}")
elif choice== 1:
    print(f"your choice: {paper}")
elif choice== 2:
    print(f"your choice: {scissors}")

import random
game=["rock","paper","scissors"]

index= random.randint(0,2)


if index == 0:
    print(f"computer choice: {rock}")
elif index == 1:
    print(f"computer choice: {paper}")
elif index == 2:
    print(f"computer choice: {scissors}")

if choice == 0 and index == 2:
    print("you won")
elif choice == 1 and index == 0:
    print("you won")
elif choice==2 and index == 1:
    print("you won")
elif choice == 0 and index==1:
    print("game over")
elif choice== 1 and index ==2:
    print("game over")
elif choice == 2 and index == 0:
    print("game over")





# game_images = [rock, paper, scissors]
# if user
# print(game_images[0])
# import random
# user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# #0,1 or 2
# computer_choice= random.randint(0,2)
# # print(f"Computer chose: {computer_choice}")
#
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number. You lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
