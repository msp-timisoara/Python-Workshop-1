from turtle import *
import random
turtle = Turtle()
"""
print('What distance do you want?')
n = int(input())
"""
n = 10
j = 0
#set up the canvas
canvas = Screen()
canvas.setup(600,400)
canvas.bgcolor("skyblue")

turtle.speed(10)
#turtle.forward(25)
#turtle.left(30)

for i in range(0,n):
    turtle.forward(i)
"""
while(j < n): # infinite loop
    #i = i -1 #backwards infinite loop
    j = j + 1
    turtle.forward(i/2)
    turtle.left(i)
"""
def random_color():
    R = random.random()
    G = random.random()
    B = random.random()

    turtle.color(R, G, B)
def move_foward(x):#functions
    if (x < 0):
        return 0
    turtle.forward(x)
    random_color()
    turtle.left(x-1)
    #recusion
    move_foward(x-1)
move_foward(10)

canvas.exitonclick()