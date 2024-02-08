from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = self.fetch_highscore()
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
            self.update_highscore()
        self.score = 0
        self.update_score()

    def update_highscore(self):
        with open("./Snake Game/highscore.txt", "w") as file:
            file.write(str(self.highscore))

    def fetch_highscore(self):
        with open("./Snake Game/highscore.txt", "r") as file:
            self.highscore = int(file.readline())

        return self.highscore
