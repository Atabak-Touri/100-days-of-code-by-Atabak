import random
from tkinter.font import names

from art import logo
from art import vs
from game_data import data

A = random.choice(data)
B = random.choice(data)






continue_game = True

def compare(guess):
    score = 0
    if A_follower > B_follower and guess == 'A':
        return True
        # score = 1
        # print(f"You're right! Current score: {score}")
    elif B_follower > A_follower and guess == 'B':
        return True
        # score = 1
        # print(f"You're right! Current score: {score}")
    else:
        continue_game = False
score = 0

while continue_game:
    A = B
    if A == B:
        B = random.choice(data)
    A_follower = int(A['follower_count'])
    B_follower = int(B['follower_count'])

    print(f"Compare A: {A['name']},a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Against B: {B['name']},a {B['description']}, from {B['country']}")
    print(A_follower)
    print(B_follower)
    guess= input("Who has more followers? Type 'A' or 'B': ")
    correct_guess= compare(guess)
    if correct_guess == True:
        score+=1
        print(f"You're right! Current score: {score}")
    else:
        print("You lose!")
        continue_game = False

