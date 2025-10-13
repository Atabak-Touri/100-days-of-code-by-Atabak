# Logic-only Snake class for Kivy
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = (0, 1)
DOWN = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)

class Snake:
    def __init__(self):
        self.segments = list(STARTING_POSITION)
        self.direction = RIGHT
    @property

    def head(self):
        return self.segments[0]
    
    def move(self):
        new_segments = [
            (self.segments[i - 1][0], self.segments[i - 1][1])
            for i in range(1, len(self.segments))
        ]
        # Move head
        new_head = (
            self.head[0] + self.direction[0] * MOVE_DISTANCE,
            self.head[1] + self.direction[1] * MOVE_DISTANCE
        )
        self.segments = [new_head] + new_segments

    def set_direction(self, direction):
        # Prevent reversing
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction
    
    def up(self):
        self.set_direction(UP)
    def down(self):
        self.set_direction(DOWN)
    def left(self):
        self.set_direction(LEFT)
    def right(self):
        self.set_direction(RIGHT)
    def extend(self):
        # Add a new segment at the position of the last segment
        self.segments.append(self.segments[-1])
