# import turtle as t
# from random import choice
# multiples = []
# for i in range(-12, 12):
#     multiples.append(i*20)
#
#
# class Food:
#     def __init__(self):
#         self.score_not_goaled = True
#         self.food = t.Turtle('circle')
#         self.food.color('pink')
#         self.food.setposition(50.0, 50.0)
#
#     def print_food(self):
#         self.food.pu()
#         self.food.setposition(choice(multiples)/1, choice(multiples)/1)

from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('pink')
        self.speed('fastest')
        self.rand_x = randint(-260, 260)
        self.rand_y = randint(-260, 260)
        self.chg_pos()


    def chg_pos(self):
        self.rand_x = randint(-280, 280)
        self.rand_y = randint(-280, 280)
        self.goto(self.rand_x, self.rand_y)


