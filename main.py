import snake
import time
from turtle import Screen
from food import Food

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

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()


screen.exitonclick()
