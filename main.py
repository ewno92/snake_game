import snake
import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title('The Snake Game')
screen.tracer(0)
# segment_1 = turtle.Turtle("square")
# segment_1.color('white')
snake = snake.Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# segment_1 = turtle.Turtle("square").color('white')

food = Food()
scoreboard = Scoreboard()
game_on = True


while game_on:
    screen.update()
    snake.doublePressLock = 0
    time.sleep(0.05)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if (snake.head.xcor() > 280) or (snake.head.xcor() < -280) or (snake.head.ycor() > 280) or (snake.head.ycor() < -280):
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
