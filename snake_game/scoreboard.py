from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read()) #read() is always str! here we need to convert it
        self.color("white")
        self.penup()
        self.goto(0, 165)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"score:{self.score} high score: {self.high_score}" , align="center",font=("Arial",15,"normal"))
        #I can make constant in the beggining as ALIGNMENT='center' and FONT=("Arial",15,"normal")
        #this line would then look like this(prevent hard coding):
        #self.write(f"score:{self.score}", align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.clear()
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0 #this line needs to be triggered afterward, because if it works in the beginning, it will always be less than high score
        self.update_scoreboard()
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center",font=("Arial",30,"normal"))
