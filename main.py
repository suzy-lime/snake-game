from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# SCREEN SET UP
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SneakySnake")
screen.tracer(0)

# OBJECTS
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# LISTEN AND KEYS
screen.listen()
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)

# GAMEPLAY
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.color_refresh()
        food.refresh()
        scoreboard.increase_score()
        snake.add_segment()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.restart()
        scoreboard.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.restart()
            scoreboard.reset()

screen.exitonclick()
