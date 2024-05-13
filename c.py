
# import turtle
# turtle.hideturtle()

# def rectangle(height,width):
#     w=width
#     h=height
#     turtle.pencolor(input("border color : "))
#     for i in range(2):
#         turtle.forward(h)
#         turtle.left(90)
#         turtle.forward(w)
#         turtle.left(90)
# h=int(input("height of rectangle : "))
# w=int(input("width of rectangle : "))
# rectangle(h,w)
# turtle.done()
import turtle

import random

t=turtle.Turtle()
# t = turtle.Pen() 

t.shape("turtle")
t.speed(0)
turtle.bgcolor("black") 
a=0
for x in range(350): 
    a=a+1
    # t.pencolor(colors[x%6]) 
    t.pencolor('#%06x' % random.randint(0, 2**24 - 1))
    t.width(a//180 + 1) 
    t.forward(x) 
    t.right(59)#t.right(100 or anything)

t.goto(0,0)
t.write("Atikur",align="center",font=("",150,""))
turtle.done()

# screen = turtle.Screen()
# screen.bgcolor("black")

# # Create a Turtle object
# pen = turtle.Turtle()
# pen.speed(0)
# pen.color("cyan")

# # Draw an Archimedean spiral
# angle = 0
# for _ in range(100):
#     pen.forward(angle)
#     pen.right(20)
#     angle = angle+1

# # Hide the turtle
# pen.hideturtle()

# # Keep the window open
# screen.mainloop()
