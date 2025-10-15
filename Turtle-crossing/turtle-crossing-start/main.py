import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.listen()
    screen.onkey(turtle.up, "Up")
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    #collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20 :
            game_is_on = False


screen.exitonclick()
