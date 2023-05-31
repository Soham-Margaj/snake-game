from turtle import Turtle

FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('../../highscore.txt', mode='r') as file:
            self.temp = file.read()
        self.highscore = int(self.temp)
        self.high_score()
        self.goto(0, 240)

        self.shapesize(stretch_wid=10, stretch_len=10)
        self.hideturtle()
        self.color('white')
        self.write(arg=f"Score: {self.score}", move=True, align='center', font=FONT)

    def new_score(self):
        self.score += 1
        self.high_score()
        self.goto(0, 240)
        self.write(arg=f"Score: {self.score}", move=True, align='center', font=FONT)

    def high_score(self):
        self.clear()
        if self.highscore < self.score:
            self.highscore = self.score
        self.goto(-200, 240)
        self.write(arg=f"Highscore: {self.highscore}", move=True, align='center', font=FONT)
        with open('/Users/Admin/Desktop/highscore.txt', mode='w') as file:
            file.write(f"{self.highscore}")
