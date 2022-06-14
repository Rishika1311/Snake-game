import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = t.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
is_True = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while is_True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.squares[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.squares[0].xcor() > 280 or snake.squares[0].xcor() < -280 or snake.squares[0].ycor() > 280 or snake.squares[0].xcor() < -280:
        is_True = False
        scoreboard.game_over()
    for segments in snake.squares[1:]:
        if snake.squares[0].distance(segments) < 10:
            is_True = False
            scoreboard.game_over()
screen.exitonclick()
