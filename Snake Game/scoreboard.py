from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(
            f"Score : {self.score} | Highscore : {self.highscore}",
            align="center",
            font=(
                "Arial",
                24,
                "normal",
            ),
        )

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()
            
        
        
