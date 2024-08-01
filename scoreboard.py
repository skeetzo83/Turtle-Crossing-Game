from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-300, 300)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 250)
        self.write(f"Level: {self.level}", align="Left", font=(FONT))

    def add_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        game = Turtle()
        game.hideturtle()
        game.write("Game Over", align="center", font=(FONT))