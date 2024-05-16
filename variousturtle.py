# import turtle as t
# import random
# t.color('#%06x' % random.randint(0, 2**24 - 1))
# t.write("you create, and more.", align="center", font=("" ,20, ""))
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
a=0
for x in range(350): 
    a=a+1
    # t.pencolor(colors[x%6]) 
    t.pencolor('#%06x' % random.randint(0, 2**24 - 1))
    t.width(a//180 + 1) 
    t.forward(x) 
    t.right(59)
    t.goto(0,0)
turtle.done()