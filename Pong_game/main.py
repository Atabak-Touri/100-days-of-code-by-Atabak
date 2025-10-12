from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen= Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle= Paddle()
right_paddle.goto(350,0)
left_paddle= Paddle()
left_paddle.goto(-350,0)
left_paddle.color("red")

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

ball= Ball()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()