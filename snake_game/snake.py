from turtle import Turtle
STARTING_POSITION=[(0,0),(-20,0),(-40,0)] #this is my constant and in python the constants should be written in cap slock
MOVE_DISTANCE= 20 #if we want to change these constants then it is much more convenient to do it here rather than our codes body
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self): #what should happen when we initialize a new snake object:
        self.snakes = [] #starting with new attribute that is associated with our snake class
        # when we're working in a class we need to work within self
        self.create_snake()
        self.head=self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
 #in order to refer to our attribute snakes, we need this self

    def move(self):
        for snk_num in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[snk_num - 1].xcor()  # returns x coordinate
            new_y = self.snakes[snk_num - 1].ycor()  # returns y coordinate
            self.snakes[snk_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN :
           self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP :
           self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT :
           self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT :
           self.head.setheading(RIGHT)
    def extend(self):
        self.add_segment(self.snakes[-1].position()) #this will add the new segment to the position of last segment
    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)
    def reset(self):
        for seg in self.snakes:
            seg.goto(10000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]
