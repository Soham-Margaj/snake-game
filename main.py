import turtle as t
import snake
import food
# import random as r
import time
import scoreboard

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)
snakes = snake.Snake()
food = food.Food()
score = 0
display = scoreboard.Scoreboard()
screen.update()
game_on = True
screen.listen()
screen.onkey(snakes.rt, 'Right')
screen.onkey(snakes.lf, 'Left')
screen.onkey(snakes.up, 'Up')
screen.onkey(snakes.dw, 'Down')
while True:

    snakes.move()
    if game_on==False:
        snakes.head.goto(0, 0)
        game_on = True
        display.score = -1
        display.new_score()

    game_on = snakes.game()
    if snakes.head.distance(food) < 15:
        food.chg_pos()
        snakes.extend()
        display.new_score()
        print(display.score)
    for (snake) in snakes.all_snake[1:len(snakes.all_snake)-1]:
        if snakes.head.distance(snake) < 10:
            print('true')
            snakes.head.goto(0, 0)
            snakes.del_snake()
            display.score = -1
            display.new_score()

    screen.update()
    time.sleep(0.1)
screen.exitonclick()
