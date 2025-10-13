class Scoreboard:
    def __init__(self):
        self.score = 0
        self.game_over_flag = False

    def increase_score(self):
        self.score += 1
    
    def game_over(self):
        self.game_over_flag = True
