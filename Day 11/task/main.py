import random
# from turtledemo.nim import computerzug

def deal_card():
    """returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card= random.choice(cards)
    return card


def calculate_score(cards):
    """take the sum of cards and give back scores"""
    if sum(cards)== 21 and  len(cards)== 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1) #remove 11 and replace it with one

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Loose"
    elif u_score == 0:
        return "Win"
    elif u_score > 21:
        return "You went over! LOSE"
    elif c_score > 21:
        return ("Computer went over! WIN!")
    elif u_score > c_score:
        return "You win"
    else:
        return "you lose!"


user_cards = []
computer_cards = []
computer_score = -1
user_score = -1

is_game_over= False
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"your card is : {user_cards}, current score: {user_score}")
    print(f"computer's first card is: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21 :
        is_game_over = True
    else:
        user_should_deal= input("type y to get a card and n tp just pass.")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over= True
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)

print(compare(user_score, computer_score))