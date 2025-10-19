import os
PLACE_HOLDER= "[name]"

with open("./Input/Names/invited_names.txt") as names:
    my_guests= names.readlines() #returns a list containing each line in the file as a list item.

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents= letter_file.read()
    for name in my_guests:
        stripped_name = name.strip()
        new_invitation= letter_contents.replace(PLACE_HOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode= "w") as completed_invitation:
            completed_invitation.write(new_invitation)