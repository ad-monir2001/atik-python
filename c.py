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

# import turtle
# t=turtle.Turtle()
# t.hideturtle()
# t.color("green")
# t.begin_fill()
# t.penup()
# t.goto(0,50)
# t.pendown()
# for i in range(6):
#   t.forward(100)
#   t.right(60)
# t.end_fill()

# import math

# t.goto(50,-(math.sqrt(6400)))
# t.color("red")
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# turtle.exitonclick()

import turtle
import random
t=turtle.Turtle()
t.color('#%06x' % random.randint(0, 2**24 - 1))
t.begin_fill()
t.circle(50)
t.end_fill()
t.color('#9999ff')
t.goto(0,-80)
t.shape("turtle")
t.forward(200)
# import turtle
# t=turtle.Turtle()
# import random
# t.penup()
# t.goto(-170,150)
# t.write("Create Your Free Account","center",None,"25pt bold")
# t.goto(-140,120)
# t.write("'Let's get started! Your free account","center",None,"18pt bold")
# t.goto(-140,100)
# t.write(" will let you create trinkets, see ","center",None,"18pt bold")
# t.goto(-140,80)
# t.write("interaction statistics for each trinket","center",None,"15pt bold")
# t.goto(-140,60)
# t.write(" you create, and more.","center",None,"18pt bold")
turtle.exitonclick()
