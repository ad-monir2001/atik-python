# import turtle 
# t=turtle.Turtle()
# t.hideturtle()
# t.color("green")
# t.begin_fill()
# for i in range(2): 
#     t.forward(150)
#     t.right(90)
#     t.forward(100)
#     t.right(90)
# t.end_fill()
# t.penup()
# t.goto(90,-50)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(20)

# t.end_fill()
# turtle.exitonclick()

# ! HOME work

# make a hexagonal (sorovuj)

import turtle
t=turtle.Turtle()
t.hideturtle()
t.color("green")
t.begin_fill()
t.goto(0,50)
for i in range(6):
  t.forward(100)
  t.right(60)
t.end_fill()
t.penup()
import math
t.goto(50,-(math.sqrt(6400)))
t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()
turtle.exitonclick()
