import time
from turtle import Screen, Turtle
from snake import Snake


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # :until we are not commanding update it will not show what's happening afterward. I need this statement
#to prevent the snakes moving apart

snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


#when we want sth to continuously happen we use while loop:
game_is_on= True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# screen.update(): if I put it here, they will never show up as they go forward to infinity and I will never reach the
# update statement. so I should put it before the for loop





screen.exitonclick()

# snake= Turtle(shape="square")
# snake.color("white")
# snake1= Turtle(shape="square")
# snake1.color("white")
# snake1.goto(-20,0)
# snake2= Turtle(shape="square")
# snake2.color("white")
# snake2.goto(-40,0)