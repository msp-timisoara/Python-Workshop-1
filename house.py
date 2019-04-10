# Create a scene with a house, a tree, and a sun
# Based on the picture at http://dragonometry.net/blog/?p=566

import turtle
import math

# Set the background color
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create our turtle
t = turtle.Turtle()
t.color("black")
t.shape("turtle")
t.speed(10)


# Define a funtion to draw and fill a rectangle with the given
# dimensions and color
class Rectangle():
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def drawRectangle(t, width, height, color):
        t.fillcolor(color)
        t.begin_fill()
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.end_fill()


# Define a function to draw and fill an equalateral right
# triangle with the given hypotenuse length and color.  This
# is used to create a roof shape.
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()


# Define a function to draw and fill a parallelogram, used to
# draw the side of the house
def drawParallelogram(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.left(30)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(120)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(90)
    t.end_fill()


# Define a function to draw four sun rays of the given length,
# for the sun of the given radius.  The turtle starts in the
# center of the circle.
def drawFourRays(t, length, radius):
    for i in range(4):
        t.penup()
        t.forward(radius)
        t.pendown()
        t.forward(length)
        t.penup()
        t.backward(length + radius)
        t.left(90)


# Draw and fill the front of the house
t.penup()
t.goto(-150, -120)
t.pendown()
Rectangle.drawRectangle(t, 100, 110, "blue")

# Draw and fill the front door
t.penup()
t.goto(-120, -120)
t.pendown()
Rectangle.drawRectangle(t, 40, 60, "lightgreen")

# Front roof
t.penup()
t.goto(-150, -10)
t.pendown()
drawTriangle(t, 100, "magenta")

# Side of the house
t.penup()
t.goto(-50, -120)
t.pendown()
drawParallelogram(t, 60, 110, "yellow")

# Window
t.penup()
t.goto(-30, -60)
t.pendown()
drawParallelogram(t, 20, 30, "brown")

# Side roof
t.penup()
t.goto(-50, -10)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.left(30)
t.forward(60)
t.left(105)
t.forward(100 / math.sqrt(2))
t.left(75)
t.forward(60)
t.left(105)
t.forward(100 / math.sqrt(2))
t.left(45)
t.end_fill()

# Tree base
t.penup()
t.goto(100, -130)
t.pendown()
Rectangle.drawRectangle(t, 20, 40, "brown")

# Tree top
t.penup()
t.goto(65, -90)
t.pendown()
drawTriangle(t, 90, "lightgreen")
t.penup()
t.goto(70, -45)
t.pendown()
drawTriangle(t, 80, "lightgreen")
t.penup()
t.goto(75, -5)
t.pendown()
drawTriangle(t, 70, "lightgreen")

# Sun
t.penup()
t.goto(55, 110)
t.fillcolor("yellow")
t.pendown()
t.begin_fill()
t.circle(24)
t.end_fill()

# Sun rays
t.penup()
t.goto(55, 134)
t.pendown()
drawFourRays(t, 25, 24)
t.right(45)
drawFourRays(t, 15, 24)
t.left(45)

# Put down some labels
t.color("black")
t.penup()
t.goto(-150, 70)
t.pendown()
t.write("House", "14pt bold")
t.penup()
t.goto(150, -150)
t.pendown()
t.write("Tree", "14pt bold")
t.penup()
t.goto(130, 150)
t.pendown()
t.write("Sun", "14pt bold")

# Bring the turtle down to the front door, and we're done!
t.penup()
t.goto(-100, -150)
t.left(90)

screen.exitonclick()