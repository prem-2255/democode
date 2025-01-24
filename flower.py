import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle object
flower_turtle = turtle.Turtle()
flower_turtle.speed(0)

# Function to draw a petal
def draw_petal(turtle, radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.end_fill()

# Function to draw the flower
def draw_flower(turtle, num_petals):
    for i in range(num_petals):
        hue = i / num_petals
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        draw_petal(turtle, 100, color)
        turtle.left(360 / num_petals)

# Function to draw the center of the flower
def draw_center(turtle, radius):
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Draw the flower
flower_turtle.penup()
flower_turtle.goto(0, -50)
flower_turtle.pendown()
draw_flower(flower_turtle, 12)

# Draw the center of the flower
flower_turtle.penup()
flower_turtle.goto(0, -20)
flower_turtle.pendown()
draw_center(flower_turtle, 20)

# Hide the turtle and finish
flower_turtle.hideturtle()
turtle.done()