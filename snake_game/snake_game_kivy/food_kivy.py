import random
class Food:
    def __init__(self, min_x=-190, max_x=190, min_y=-190, max_y=190):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.position = (0, 0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(self.min_x, self.max_x)
        random_y = random.randint(self.min_y, self.max_y)
        self.position = (random_x, random_y)