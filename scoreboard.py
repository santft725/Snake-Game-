from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 13, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def make_score(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.make_score()


