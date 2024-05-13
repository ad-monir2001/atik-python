#! HOME work
#Home wark 1
# *Draw a rectangle .The length of that rectangle is a and width is b. a and b are an integer number which will be chosen by the user.
import turtle
t=turtle.Turtle()
t.hideturtle()
a=int(input("Please take a length to draw a rectangle : "))
b=int(input("Please take a width to draw a rectangle : "))

if a!=b:
    t.begin_fill()
    color=input("filled color ")
    t.pencolor(input("border color ; "))
    t.width()
    for i in range(2):


        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)
    t.end_fill()
else:
    print("To draw a rectangle, the length and width will not be equal.")
turtle.done()