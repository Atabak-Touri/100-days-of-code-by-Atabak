import random
from art import logo

EASY_LEVEL_ATTEMPS= 10
HARD_LEVEL_ATTEMPS=5

def check(user_guess, answer, attempts):
    if user_guess > answer:
        print("Too High. Try again!")
        return attempts -1
    elif user_guess < answer:
        print("Too low. Try again!")
        return attempts - 1
    else:
        print(f"You got this! The answer is {answer}")

def level_set():
    level = input("which level you want to guess? easy or hard?")
    if level == "easy":
        return EASY_LEVEL_ATTEMPS
    elif level == "hard":
        return HARD_LEVEL_ATTEMPS

def game():
    print(logo)
    print("Welcome to number guessing game!")
    print("I am thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    print(f"Psst, the correct answer is {answer}")

    attempts= level_set()
    user_guess = 0
    while user_guess != answer:
        print(f"You have {attempts} left to guess!")
        user_guess = int(input("Guess a number: "))
        attempts = check(user_guess, answer, attempts)
        if attempts == 0:
            return
        elif user_guess != answer:
            print("Guess again!")

game()
