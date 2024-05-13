# # #!Home wark 2
# #*Draw a circle with a radius chosen by the user, and  filled the circle with a color which also chosen by the user 
import turtle
t=turtle.Turtle()
t.hideturtle()
r=int(input("radius of circle : "))
color=input("Choose a color which color will filled with a circle : ")
t.begin_fill()
t.circle(r)
t.color(color)
t.end_fill()
turtle.done()