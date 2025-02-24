import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=900, height=600)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# Creating border
border = turtle.Turtle()
border.speed(5)
border.pensize(4)
border.penup()
border.goto(-310, 250)
border.pendown()  # Start drawing
border.color("red")
for _ in range(2):
    border.forward(600)
    border.right(90)
    border.forward(500)
    border.right(90)
border.penup()
border.hideturtle()

# Score
score = 0
delay = 0.1

# Scoring display
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: 0", align="center", font=("Courier", 24, "bold"))

# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# Food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

# Movement functions
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard controls
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# Main loop
while True:
    screen.update()
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        
        score += 1
        scoring.clear()
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

        delay = max(0.05, delay - 0.001)  # Prevent delay from going too low

        # Create new segment
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # Move body
    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()
        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)

    snake_move()

    # Snake & border collisions
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write("Game Over\nYour score is {}".format(score), align="center", font=("Courier", 24, "bold"))
        break  # Exit loop when game over

    # Snake collisions with itself
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write("Game Over\nYour score is {}".format(score), align="center", font=("Courier", 24, "bold"))
            break  # Exit loop when game over

    time.sleep(delay)
turtle.done()