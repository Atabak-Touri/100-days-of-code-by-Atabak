from turtle import Turtle

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.penup()
    #
    # def create_pong(self):
    #     for pos in POSITION:
    #         pong = Turtle()
    #         pong.shape("square")
    #         pong.color("white")
    #         pong.shapesize(stretch_wid=5,stretch_len=0.5)
    #         pong.penup()
    #         pong.goto(pos)

    # def move(self):
    #
    #     new_y = PONG.ycore() + 20
    #     go_up = PONG.goto()

