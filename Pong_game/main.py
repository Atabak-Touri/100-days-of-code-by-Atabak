from turtle import Screen, Turtle
from pongs import Pong

screen= Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.bgcolor("black")


pong= Pong()
right_pong= pong.pos(350,0)
left_pong = pong.pos(-350,0)
def go_up():
    new_y= pong.ycor()+ 20
    pong.goto(pong.xcor(),new_y)
def go_down():
    new_y= pong.ycor() - 20
    pong.goto(pong.xcor(),new_y)
screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")


screen.exitonclick()