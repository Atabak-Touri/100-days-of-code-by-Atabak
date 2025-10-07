import random
word_list=["aardvark","baboon","camel"]

chosen_word=random.choice(word_list)
print(chosen_word)

place_holder=""
for letter in chosen_word:
    place_holder+= ("_")
print(place_holder)


game_over=False
correct_words=[]
while not game_over:
    guess=input("guess a word:\n")
    display=""
    for word in chosen_word:
        if guess==word:
            display+=guess
            correct_words.append(guess)
        elif word in correct_words:
            display+= word
        else:
            display+="_"

    print(display)

    if "_" not in display:
        game_over=True
        print("you win.")