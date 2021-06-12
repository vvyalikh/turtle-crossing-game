from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.level = 1

    def update_level(self):
        self.clear()
        self.goto(x=-250, y=250)
        self.write(f"LEVEL{self.level}", align= "left", font=FONT)

    def new_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

