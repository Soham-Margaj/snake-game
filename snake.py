import turtle as t


class Snake:
    def __init__(self):
        self.snake = None
        self.start_pos = [(0, 0), (-15, 0), (-30, 0)]
        self.all_snake = []

        for pos in self.start_pos:
            self.snake = t.Turtle(shape='square')
            self.snake.color('white')
            self.snake.speed('slowest')
            self.snake.shapesize(stretch_wid=0.75, stretch_len=0.75)
            self.snake.setposition(pos)
            self.snake.pu()
            self.all_snake.append(self.snake)
        self.head = self.all_snake[0]

    def make_snake(self, position):
        self.snake = t.Turtle(shape='square')
        self.snake.color('white')
        self.snake.speed('slowest')
        self.snake.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.snake.hideturtle()
        self.snake.pu()
        self.snake.setposition(position)
        self.all_snake.append(self.snake)

    def extend(self):
        self.make_snake(self.all_snake[len(self.all_snake) - 1].position())

    def move(self):
        for i in range(len(self.all_snake) - 1, 0, -1):
            self.all_snake[i].showturtle()
            goto_pos = self.all_snake[i - 1].pos()
            self.all_snake[i].goto(goto_pos)
        self.all_snake[0].fd(15)

    def rt(self):
        if self.head.heading() != 180:
            self.all_snake[0].setheading(0)

    def lf(self):
        if self.head.heading() != 0:
            self.all_snake[0].setheading(180)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def dw(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def game(self):
        if abs(self.all_snake[0].xcor()) >= 280 or abs(self.all_snake[0].ycor()) >= 280:
            self.del_snake()
            return False
        else:
            return True

    def del_snake(self):
        for i in range(len(self.all_snake) - 1, 2, -1):
            self.all_snake[i].hideturtle()
            self.all_snake.remove(self.all_snake[i])



