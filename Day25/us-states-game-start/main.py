import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)



def get_mouse_click_coor(x, y): #this will show my mouse coordination on screen
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor) #event listen

turtle.mainloop() #alternative way to keep the screen open


screen.exitonclick()