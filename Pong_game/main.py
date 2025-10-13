from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score_board
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

scoreboard = Score_board()

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

ball= Ball()
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #collision with wall. when the y axis is higher than 300, it definitely hit the wall
    if ball.ycor() > 280 or ball.ycor()<-280:
        #needs to bounce(needs to be defined in the Ball class)
        ball.bounce_y()

    #collision with the paddle
    if ball.distance(right_paddle)< 50 and ball.xcor()> 340 or ball.distance(left_paddle)< 50 and ball.xcor()< -320:
        ball.bounce_x()
    #misiing the ball on right side
    if ball.xcor()> 380:
        ball.reset_position()
        scoreboard.l_point()
    #misiing the ball on the left side
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()