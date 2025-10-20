import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data= pandas.read_csv("50_states.csv")
all_states= data.state.to_list()

guessed_states= []

while len(guessed_states)< 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="what's the state's name?").title() #title() will make the first letter in capital

    # if the answer_state is one of the states in our csv file
    if answer_state == "Exit":
        missing_state= []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        print(missing_state)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
    # if it is, make the turtle to write the name of the state on the location
        t.write(answer_state)
#states to learn

# def get_mouse_click_coor(x, y): #this will show my mouse coordination on screen
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor) #event listen
#
# turtle.mainloop() #alternative way to keep the screen open


screen.exitonclick()