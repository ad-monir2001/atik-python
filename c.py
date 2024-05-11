# t.color('#%06x' % random.randint(0, 2**24 - 1))
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.color('#9999ff')
# t.goto(0,-80)
# t.shape("turtle")
# t.forward(200)
# import turtle
# t=turtle.Turtle()
# import random
# t.penup()
# t.goto(-170,150)
# t.write("you create, and more.", align="center", font=("" ,20, ""))
# ! HOME work
#!Home wark 1
# # *Draw a rectangle .The length of that rectangle is a and width is b. a and b are an integer number which will be chosen by the user.
import turtle
t=turtle.Turtle()
a=int(input("Please take an integer number : "))
b=int(input("Please take an another integer number : "))
if a!=b:
    for i in range(2):

        t.pencolor("red")
        t.width(2)
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)
else:
    print("To draw a rectangle, the length and width will not be equal.")

# #!Home wark 2
#*Draw a circle with a radius chosen by the user, and  filled the circle with a color which also chosen by the user 
# import turtle
# t=turtle.Turtle()
# t.hideturtle()
# r=int(input("radius of circle : "))
# color=input("Choose a color which color will filled with a circle : ")
# t.pencolor("black")
# t.width(2)
# t.begin_fill()
# t.circle(r)
# t.color(color)
# t.end_fill()
# turtle.done()


